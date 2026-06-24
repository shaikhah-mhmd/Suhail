from sklearn.linear_model import LinearRegression
def predict_next_days(days, electricity, n=7):
  model=LinearRegression()
  model.fit(days,electricity)
  last_day=days[-1][0]
  future=[[last_day+i]for i in range(1,n+1)]
  return model.predict(future)

