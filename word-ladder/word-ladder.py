class Solution:

    def update_graph_for_word(self, graph: dict, beginWord: str, wordList: List[str], englishChars: List[str]):
        
        for i in range(len(beginWord)):
            for char in englishChars: # 28 chars
                if char != beginWord[i]:
                    new_word = beginWord[:i] + char + beginWord[i+1:]
                    if new_word in wordList:
                        graph[new_word].add(beginWord)
                        graph[beginWord].add(new_word)
        return graph

    def find_shortest_path_bfs(self, initial_word, target_word, graph):

        queue = [(initial_word, 1)]
        visited = defaultdict(int)
        while len(queue) != 0 :
            (cur_nod , level) = queue.pop(0)

            if cur_nod == target_word:
                return level

            cur_nod_children = graph[cur_nod]
            queue += list([ (child, level + 1) for child in cur_nod_children if visited[child] != 1])
            visited[cur_nod] = 1
        return 0

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        graph = defaultdict(set)
        englishChars = [chr(char_asci) for char_asci in range(ord('a'), ord('z') + 1)]
      
        wordList = set(wordList)
        graph = self.update_graph_for_word(graph, beginWord, wordList, englishChars )
        for word in wordList:
            graph = self.update_graph_for_word(graph, word, wordList, englishChars )
        
        # print('Graph')
        # return
        level =  self.find_shortest_path_bfs(beginWord, endWord, graph)
        
        return level 
        
