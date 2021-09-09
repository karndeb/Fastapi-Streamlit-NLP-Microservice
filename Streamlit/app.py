from multiapp import MultiApp
from apps import fr, nqr, qe

app = MultiApp()
fr_api_call = fr.MakeCalls()
nqr_api_call = nqr.MakeCalls()
qe_api_call = qe.MakeCalls()

# Add all your application here
app.add_app("Fallback Reduction", fr_api_call.app)
app.add_app("Next Query Recommendation", nqr_api_call.app)
app.add_app("Query Expansion", qe_api_call.app)

# The main app
app.run()

