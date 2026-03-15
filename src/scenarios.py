from __future__ import annotations
from typing import Dict, List


def get_scenarios() -> List[Dict]:
    """
    Definicija simulacionih scenarija za analizu toplotne razmjene
    između dva tijela.
    """
    return [

        
        # Scenario A: Simetrične toplotne mase (C1 = C2)
        
        {
            "name": "Scenario A: Simetrične toplotne mase (C1 = C2)",
            "m1": 2.0,   "c1": 500.0,
            "m2": 1.0,   "c2": 1000.0,
            "T1": 80.0,  "T2": 20.0,
            "K": 50.0,
            "t_end": 60.0,
            "dt": 0.5,
        },

        
        # Scenario B1: Velika razlika toplotnih masa (C1 >> C2),
        #              tijelo T1 je inicijalno toplije
        
        {
            "name": "Scenario B1: Velika razlika toplotnih masa (C1 >> C2), T1 toplije",
            "m1": 2.5,   "c1": 500.0,
            "m2": 2.0,   "c2": 500.0,
            "T1": 80.0,  "T2": 20.0,
            "K": 50.0,
            "t_end": 60.0,
            "dt": 0.5,
        },

        
        # Scenario B2: Velika razlika toplotnih masa (C1 >> C2),
        #              tijelo T1 je inicijalno hladnije
        
        {
            "name": "Scenario B2: Velika razlika toplotnih masa (C1 >> C2), T1 hladnije",
            "m1": 2.5,   "c1": 500.0,
            "m2": 2.0,   "c2": 500.0,
            "T1": 20.0,  "T2": 80.0,
            "K": 50.0,
            "t_end": 60.0,
            "dt": 0.5,
        },

    
        # Scenario C: Slaba termička veza (mali K)
        
        {
            "name": "Scenario C: Slaba termička veza (mali K)",
            "m1": 1.0,   "c1": 500.0,
            "m2": 1.0,   "c2": 500.0,
            "T1": 80.0,  "T2": 20.0,
            "K": 5.0,
            "t_end": 200.0,
            "dt": 1.0,
        },

    
        # Scenario D: Jednake toplotne mase, velika početna razlika temperatura
             
       {
            "name": "Scenario D: Jednake toplotne mase, velika početna razlika temperatura",
            "m1": 1.0,    "c1": 1000.0,
            "m2": 1.0,    "c2": 1000.0,
            "T1": 150.0,  "T2": 0.0,
            "K": 50.0,
            "t_end": 80.0,
            "dt": 0.5,
        },
    ]
