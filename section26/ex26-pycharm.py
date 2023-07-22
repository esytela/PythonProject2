import sklearn

print(sklearn._version_)

from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

import pandas as pd


# 데이터프레임 생성
data = pd.DataFrame(data=iris['data'], columns=iris['feature_names'])
target = pd.DataFrame(data=iris['target'], columns=['target'])

df = pd.concat([data, target], axis=1)

df.to_csv('iris.csv', index=False)

df = pd.read_csv('iris.csv')

# 학습데이터, 테스트데이터 분류
X_train, X_test, y_train, y_test = train_test_split(data, target,
                                                    text_size=0.2, random_state=11)
    #test 데이터 -> 테스트데이터 20%
    #train 데이터 -> 학습데이터 80%

    #X = feature 값
    #y = label/key 값

# 모델 생성
dt_clf = DecisionTreeClassifier(random_state=11)

# 학습 수행
dt_clf.fit(X_train, y_train)

pred = dt_clf.predict(X_test) #결과 값 안주고 feature 값만 줌
pred

from sklearn.metrics import accuracy_score
print('예측 정확도: {0:.4f}'.format(accuracy_score(y_test, pred)))
# 93%의 확률로 예측이 정확함

#예측하기
new_data = [[5.1, 3.0, 3, 1.2]]
new_pred = dt_clf.predict(new_data)

#학습 모델 덤프
import joblib
joblib.dump(dt_clf, 'model.joblib')
load_model.predict(new_data)