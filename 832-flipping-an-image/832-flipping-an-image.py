class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for line in image:
            self.reverse(line)
            self.invert(line)
        
        return image
        
    def reverse(self, image_line: List[int]):
        n = len(image_line)
        for i in range(n//2):
            image_line[i], image_line[-1-i] = image_line[-1-i], image_line[i]    
    
    def invert(self, image_line: List[int]):
        n = len(image_line)
        for i in range(n):
            image_line[i] = 1-image_line[i]
        