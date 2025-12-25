import numpy as np

class Solution(object):
    def imageSmoother(self, img):
        """
        :type img: List[List[int]]
        :rtype: List[List[int]]
        """
        img = np.array(img)
        S = [[0, 0, 0], [0,0,0], [0,0,0]]
        for i in range(len(img)):
            for j in range(len(img[i])):
                if j < 1 or i < 1:
                    S[i][j] = np.mean(img[0 : i+1, 0 :j +1])
                elif i == len(img) - 1 or j == len(img[i]) - 1:
                    S[i][j] = np.mean(img[i-1:i,j-1:j])
        return S

print(Solution().imageSmoother([[1,1,1],[1,0,1],[1,1,1]]))
print(([[1,1,1],[1,0,1],[1,1,1]])[1])