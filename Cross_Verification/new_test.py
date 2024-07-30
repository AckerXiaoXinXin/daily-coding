from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_iris

# 加载数据
iris = load_iris()
X = iris.data
y = iris.target

# 创建逻辑回归模型
model = LogisticRegression()

# 进行5折交叉验证
scores = cross_val_score(model, X, y, cv=5)

print("交叉验证得分：", scores)
print("平均得分：", scores.mean())


