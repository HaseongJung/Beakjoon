Ax, Ay = map(int, input().split())
Bx, By = map(int, input().split())
Cx, Cy = map(int, input().split())
Dx, Dy = 0, 0

if Ax == Bx:
    Dx = Cx
elif Bx == Cx:
    Dx = Ax
elif Ax == Cx:
    Dx = Bx

if Ay == By:
    Dy = Cy
elif By == Cy:
    Dy = Ay
elif Ay == Cy:
    Dy = By

print(Dx, Dy)