import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv('data/dataset.csv')

le_src = LabelEncoder()
le_dst = LabelEncoder()
df['src_ip_enc'] = le_src.fit_transform(df['src_ip'])
df['dst_ip_enc'] = le_dst.fit_transform(df['dst_ip'])

X = df[['src_ip_enc', 'dst_ip_enc', 'protocol', 'length']]
y = df['label']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print(classification_report(y_test, y_pred))
