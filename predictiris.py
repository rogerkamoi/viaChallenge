import numpy as np
import keras
from keras.models import Sequential


def prediction(sepallength, sepalwidth, petallength, petalwidth):

    # 1. VALIDATE INPUT DATA
    # TODO: INSERT VALIDATION CHECK ON PARAMETERS
    # if not x_test:
    # raise HTTPException(status_code=415, detail="data format.")

    # 2. LOAD THE MODEL
    model = keras.models.load_model('model/iris_model')

    # 3. CONVERT THE PARAMETERS TO NUMBERS BEFORE PRED
    X_test2 = np.array([[float(sepallength), float(
        sepalwidth), float(petallength), float(petalwidth)]])
    #X_test2 = np.array([[5, 2.5, 3, 1]])

    # 4. RUN THE PRED MODEL
    y_pred2 = model.predict(X_test2)

    # 5. CONVERT AND SEND THE RESPONSE BACK TO THE CLIENT
    # 0 = setosa 1 = versicolor 2 = virginica
    finalResponse = ['setosa', 'versicolor', 'virginica']

    # Return
    return finalResponse[int(np.argmax(y_pred2, axis=1))]


#[5, 3.9, 2, 0.5],[5,2.5,3,1],[8,3.5,6,2]
resposta = prediction(8, 3.5, 6, 2)
print(resposta)
