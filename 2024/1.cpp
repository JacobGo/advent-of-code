#include <iostream>
#include <vector>
#include <fstream>
#include <algorithm>
#include <map>

int main() {
    std::vector<int> a;
    std::vector<int> b;

    std::ifstream data("1.in");

    std::string line;
    while (getline(data, line)) {
        int mid = line.find(' ');
        a.emplace_back(std::stoi(line.substr(0, mid)));
        b.emplace_back(std::stoi(line.substr(mid + 2)));
    }

    std::sort(a.begin(), a.end());
    std::sort(b.begin(), b.end());

    int total_dist;
    for (int i = 0; i < a.size(); i++) {
        total_dist += abs(a[i] - b[i]);
    }
    std::cout << "Part 1: " << total_dist << std::endl;


    std::map<int, int> freq;
    for (int i : b) {
        auto [it, _] = freq.try_emplace(i);
        it->second++;
    }
    int similarity;
    for (int i : a) {
        similarity += i * freq[i];
    }
    std::cout << "Part 2: " << similarity << std::endl;
    return 0;
}