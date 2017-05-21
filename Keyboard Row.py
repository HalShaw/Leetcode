class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        ls=['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']
        indexs=[]
        ll=[]
        for word in words:
            index=[]
            for x in word:
                index.append(ls.index(x.lower()))
            indexs.append(index)
        for i,index in enumerate(indexs):
            if min(index)>=0 and max(index)<=9:
                ll.append(words[i])
            elif min(index)>=10 and max(index)<=18:
                ll.append(words[i])
            elif min(index)>=19 and max(index)<=25:
                ll.append(words[i])
        return ll