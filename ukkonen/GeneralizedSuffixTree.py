from SuffixTree import SuffixTree
import sys

class GeneralizedSuffixTree(SuffixTree):
	def __init__(self, strings):
		if len(strings) > 2:
			sys.exit("Currently GeneralizedSuffixTree doesn't support more than two strings!")

		self.middlePosition = len(strings[0])
		super().__init__(string='#'.join(strings))

	def longest_shared_substring(self):
		_, maxSubstring = self._longest_shared_substring_helper(self.root, [], '')

		return maxSubstring

	def shortest_non_shared_substring(self):
		_, minSubstring = self._shortest_non_shared_substring_helper(self.root, [], self.string)

		return minSubstring

	def _longest_shared_substring_helper(self, node, substringFragments, maxSubstring):
		if not all(node.get_color()):
			return substringFragments, maxSubstring
		else:
			substring = ''.join(substringFragments)
			if len(substring) > len(maxSubstring):
				maxSubstring = substring

			for child in node.get_children():
				substringFragments.append(self.string[child.get_start_position():child.get_end_position()+1])
				substringFragments, maxSubstring = self._longest_shared_substring_helper(child, substringFragments, maxSubstring)
				substringFragments.pop()

			return substringFragments, maxSubstring

	def _shortest_non_shared_substring_helper(self, node, substringFragments, minSubstring):
		if node.get_color()[1] == False:
			substring = ''.join(substringFragments)
			if len(substring) < len(minSubstring):
				minSubstring = substring
			return substringFragments, minSubstring

		else:
			for child in node.get_children():
				substringFragments.append(self.string[child.get_start_position():child.get_end_position()+1])
				substringFragments, minSubstring = self._shortest_non_shared_substring_helper(child, substringFragments, minSubstring)
				substringFragments.pop()

			return substringFragments, minSubstring

	# override
	def _set_suffix_index_by_dfs(self, node, labelLength):
		if node.is_leaf():
			if node.get_start_position() < self.middlePosition < node.get_end_position():
				node.set_end_position(self.middlePosition)

			if node.get_end_position() == self.middlePosition:
				color = [True, False]
			else:
				color = [False, True]

			node.set_color(color)
			node.set_suffix_index(len(self.string) - labelLength)
			return 1, color

		else:
			leafCount = 0
			nodeColor = [False, False]
			for child in node.get_children():
				newLabelLength = labelLength + child.get_edge_length()
				count, color = self._set_suffix_index_by_dfs(node=child, labelLength=newLabelLength)

				leafCount += count
				nodeColor = [c1 or c2 for c1, c2 in zip(nodeColor, color)]

			node.set_leaf_count(leafCount)
			node.set_color(nodeColor)
			return leafCount, nodeColor

if __name__ == '__main__':
	with open('./rosalind_ba9f.txt') as inFile:
		s1 = inFile.readline().strip()
		s2 = inFile.readline().strip()
		gst = GeneralizedSuffixTree([s1, s2])


	print(gst.shortest_non_shared_substring())
