
'''Given an 2D integer array A of size N x 2 denoting time intervals of different meetings
A[i][0] = start time of the ith meeting.
A[i][1] = end time of the ith meeting
Find the minimum number of conference rooms required so that all meetings can be done.'''

class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
        start=[]
        end=[]
        for n in  A:
            start.append(n[0])
            end.append(n[1])
        start.sort()
        end.sort()
        n=len(A)
        room = 0
        maxr = 0
        i=0
        j=0
        while(i<n and j<n):
            if(start[i]<end[j]):
                room += 1
                i += 1
            else:
                room -= 1
                j += 1
            maxr = max(maxr,room)
        return maxr
    
a = Solution()
A =  [     [1, 18],
            [18, 23],
            [15, 29],
            [4, 15],
            [2, 11],
            [5, 13]
      ]
print('Minimum Number of Meeting Hall required is  ',a.solve(A)) 