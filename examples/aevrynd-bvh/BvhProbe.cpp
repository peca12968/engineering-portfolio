#include "Aevrynd/Scene3D.h"
#include <cmath>
#include <iostream>
#include <memory>
#include <string_view>

using namespace Aevrynd;

int main() {
    constexpr std::uint32_t cells = 64, stride = cells + 1;
    auto mesh = std::make_shared<Mesh3D>();
    for (std::uint32_t z = 0; z <= cells; ++z) {
        for (std::uint32_t x = 0; x <= cells; ++x) {
            const float y = .15f * std::sin(float(x) * .2f) * std::cos(float(z) * .17f);
            mesh->vertices.push_back({float(x), y, float(z), PackNormalSnorm8({0, 1, 0}), 0xffffffffu});
        }
    }
    for (std::uint32_t z = 0; z < cells; ++z) {
        for (std::uint32_t x = 0; x < cells; ++x) {
            const auto a = z * stride + x, b = a + 1, c = a + stride, d = c + 1;
            mesh->indices.insert(mesh->indices.end(), {a, c, b, b, c, d});
        }
    }
    const auto triangles = mesh->indices.size() / 3;
    const MeshResource3D resource{MeshHandle3D{1}, mesh->Bounds(), mesh->vertices.size(), mesh->indices.size(), mesh};
    Scene3D scene;
    scene.Mesh(resource, {{}, {}, {1, 1, 1}});
    scene.Mesh(resource, {{100, 0, 0}, {0, .18f, 0}, {1.5f, 2.f, .75f}});

    std::cout << "{\"msvc\":" << _MSC_VER << ",\"triangles\":" << triangles << ",\"stages\":[";
    const auto shoot = [&](std::string_view name, Ray3D ray, std::size_t object, std::uint64_t builds) {
        const auto before = mesh->RaycastIndexBytes();
        SceneQueryStats3D stats{};
        const SceneHit3D hit = scene.Raycast(ray, 50, &stats);
        const auto after = mesh->RaycastIndexBytes();
        if (!hit || hit.objectIndex != object || stats.meshBvhBuilds != builds ||
            stats.trianglesTested != stats.meshTriangleCandidates || !stats.meshBvhNodesTested ||
            !stats.meshTriangleCandidates || stats.meshTriangleCandidates >= 128 ||
            !after || (builds ? before != 0 : before != after)) {
            std::cerr << "Unexpected BVH trace at " << name << '\n';
            return false;
        }
        std::cout << "{\"phase\":\"" << name << "\",\"object\":" << hit.objectIndex
                  << ",\"builds\":" << stats.meshBvhBuilds << ",\"candidates\":" << stats.meshTriangleCandidates
                  << ",\"nodes\":" << stats.meshBvhNodesTested << ",\"cache_before_bytes\":" << before
                  << ",\"cache_after_bytes\":" << after << '}';
        return true;
    };
    if (!shoot("first", {{20, 10, 20}, {0, -1, 0}}, 0, 1)) return 1;
    std::cout << ',';
    if (!shoot("reuse", {{120, 20, 10}, {0, -1, 0}}, 1, 0)) return 2;
    scene.TrimUnusedMemory();
    std::cout << ',';
    if (!shoot("rebuild", {{20, 10, 20}, {0, -1, 0}}, 0, 1)) return 3;
    std::cout << "]}\n";
}
