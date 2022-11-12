from explainerdashboard import ClassifierExplainer, RegressionExplainer

explainer = ClassifierExplainer(model, X_test, y_test)
explainer = RegressionExplainer(model, X_test, y_test)