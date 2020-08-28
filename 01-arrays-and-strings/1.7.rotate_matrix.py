# Rotate Matrix: Given an image represented by an NxN matrix, where each pixel 
# in the image is 4 bytes, write a method to rotate the image by 90 degrees. 
# Can you do this in place?

def rotate_matrix(img):
    N = len(img)-1

    for i in range(len(img)//2):
        for j in range(len(img)-1):
            temp          = img[j][i]
            img[j][i]     = img[i][N-j]
            img[i][N-j]   = img[N-j][N-i]
            img[N-j][N-i] = img[N-i][j]
            img[N-i][j]   = temp

    return img

test = [[ 1,  2,  3,  4],
        [ 5,  6,  7,  8],
        [ 9, 10, 11, 12],
        [13, 14, 15, 16]]

test = rotate_matrix(test)

for row in test:
    print(row)