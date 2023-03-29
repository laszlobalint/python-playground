def cough_dec(func):
  def func_wrapper():
    # Code before function
    print('*cough*')
    func()
    # Code after function
    print('*cough*')
  
  return func_wrapper

@cough_dec
def question():
  print('Can you give ma a discount on the article?')

@cough_dec
def answer():
  print('It is only 50 pounds, you cheapskate!')

question()
answer()
