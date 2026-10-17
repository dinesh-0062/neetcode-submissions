from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        groups = defaultdict(list)

        for word in strs:
            # Words with the same letters have the same sorted form.
            key = "".join(sorted(word))
            groups[key].append(word)

        return list(groups.values())


# Time Complexity: O(n * k log k), where n is the number of words
# and k is the maximum word length.
# Space Complexity: O(n * k) for storing the grouped words.
