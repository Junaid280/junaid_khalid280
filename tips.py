from explainerdashboard.custom import *

class CustomDashboard(ExplainerComponent):
    def __init__(self, explainer, name=None):
        super().__init__(explainer, name=name)
        self.dependence = ShapDependenceComponent(explainer, name=self.name+"dep",
                hide_selector=True, hide_cats=True, hide_index=True, col="Fare")

    def layout(self):
        return html.Div([self.dependence.layout()])

ExplainerDashboard(explainer, CustomDashboard).run()
                    shap_interaction=False,
                    decision_trees=False)
db.run(port=8051)