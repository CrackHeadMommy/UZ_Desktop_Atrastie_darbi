import numpy as np
import os
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
from PIL import Image

bildes = []
label = []

bilzu_adrese = "home+homes...NOT/"

for nosaukums in os.listdir(bilzu_adrese):
    image = Image.open(os.path.join(bilzu_adrese,nosaukums)).resize((200,200), Image.Resampling.NEAREST)
    bildes.append(np.array(image))
    if "NHome" in nosaukums:
        label.append(0)
    else:
        label.append(1)
    


#Jāpārtaisa par python skaitļu sarakstiem.
bildes = np.array(bildes)
label = np.array(label)

bildes = bildes/255.0 #
bildes = bildes.reshape(bildes.shape[0], -1)

X_train, X_test, y_train, y_test = train_test_split(bildes, label, test_size=0.2)



modelis = RandomForestClassifier()

modelis.fit(X_train, y_train)

paregojums = modelis.predict(X_test)

precizitate = accuracy_score(y_test, paregojums)

print(precizitate)