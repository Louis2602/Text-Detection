import cv2
import pytesseract
from googlesearch import search

pytesseract.pytesseract.tesseract_cmd = 'D:\\Tesseract-OCR\\tesseract.exe'

inputImg = input("Type in your image's name to search: ")
img = cv2.imread(inputImg)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

strList = pytesseract.image_to_string(img)  # print words from image
strList = strList[:-1]  # delete last element of the string

# Detecting characters
# def detectingCharacters():
# hImg, wImg, _ = img.shape
# boxes = pytesseract.image_to_boxes(img)
# for b in boxes.splitlines():
#     b = b.split(' ')
#     print(b)
#     x, y, w, h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
#     cv2.rectangle(img, (x, hImg-y), (w, hImg-h), (0, 0, 255), 2)
#     cv2.putText(img, b[0], (x, hImg-y + 25),
#                 cv2.FONT_HERSHEY_COMPLEX, 1, (50, 50, 255), 2)


# Detecting words
def detectingWords():
    hImg, wImg, _ = img.shape
    # conf = r'--oem 3 --psm 6 oututbase digits'  # config to detect digits
    boxes = pytesseract.image_to_data(img)
    for x, b in enumerate(boxes.splitlines()):
        if x != 0:
            b = b.split()
            print(b)
            if len(b) == 12:
                x, y, w, h = int(b[6]), int(b[7]), int(b[8]), int(b[9])
                cv2.rectangle(img, (x, y), (w+x, h+y), (0, 0, 255), 1)
                cv2.putText(img, b[11], (x, y-2),
                            cv2.FONT_HERSHEY_COMPLEX, 0.4, (50, 50, 255), 1)


# save text to file
def saveText(strList):
    print(strList)
    with open('text.txt', 'w', encoding='utf-8') as f:
        f.writelines(strList)


# save links to file
def searchAndSaveLinks(strList):
    searchLinks = []

    # searching for links in google search
    for url in search(strList, tld="com", lang='en', num=20, stop=20, pause=2):
        searchLinks.append(url+"\n")

    # store google search links into a text file
    with open('searchLinks.txt', 'w', encoding='utf-8') as f:
        f.writelines(searchLinks)


saveText(strList)
detectingWords()
searchAndSaveLinks(strList)

cv2.imshow('Result', img)
cv2.waitKey(0)
