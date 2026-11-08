// clangd uses compile_flags.txt here (or build/compile_commands.json after a cmake build).
#include <algorithm>
#include <print>
#include <vector>

int main() {
    std::vector<int> xs{5, 3, 8, 1};
    std::ranges::sort(xs);
    for (int x : xs) {
        std::println("{}", x);
    }
}
