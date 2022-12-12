# Desc: store all ml models and call them  добавляет функции в список при вызове
ml_models = []


def ml(func):
    ml_models.append(func)
    def call_func(*args, **kwargs):
        return func(*args, **kwargs)

    return call_func

@ml
def CNN():
    print('Convolutional Neural Net')

@ml
def RNN():
    print('Recurrent Neural Net')

def liner_regression():
    print('This isn`t ML')


# call all ML models
for m in ml_models:
    m()

print(ml_models)  # returns list of functions for reference