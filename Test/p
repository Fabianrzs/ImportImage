ABCD = list(string.ascii_uppercase)

print(len(ABCD))

for letter in ABCD:
    print(letter)


h = np.array([[1,0,-1], [1,0,-1], [1,0,-1]])

img = cv2.imread('pruebas.JPG')

cv2.imshow("Img Montada", img)

cv2.waitKey(0)
cv2.destroyAllWindows()


colorGray = cv2.COLOR_RGB2GRAY
imGray = cv2.cvtColor(img,colorGray)

forma = np.shape(imGray)
img2 = np.zeros(forma)


for x in list(range(1, forma[0]-1)):
    for y in list(range(1, forma[1] - 1)):
        suma = 0
        for i in list(range(-1,2)):
            for j in list(range(-1, 2)):
                suma =  imGray[x-i, y-j] * h[i+1,j+1] + suma

        img2 [x,y] = suma

maxs = np.max(img2)
img2 = img2*255/ maxs

img2 = img2.astype(np.uint8)

print(img2)