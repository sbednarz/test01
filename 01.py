def steadystate(y):
  X = y[0]
  S = y[1]
  P = y[2]
  mi = mi_max * S/(KM + S)
  rX = X * mi
  rS = -1/Y_XS * X * mi
  rP = Y_PX * X * mi
  eq1 = rX - D*X
  eq2 = D*Sf - D*S + rS
  eq3 = rP - D*P
  return [eq1, eq2, eq3]
