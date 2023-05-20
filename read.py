import cv2 as cv

img = cv.imread('Photos/cats.jpg')
cv.imshow('cat', img)


def rescaleFrame(frame, scale=0.2):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

resize = rescaleFrame(img)
cv.imshow('rescale',resize)
cv.waitKey(0)