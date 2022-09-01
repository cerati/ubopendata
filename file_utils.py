import pandas as pd

def Table2DataFrame(table):
    d1 = { k: table[k][()].flatten() for k in table.keys() if table[k].shape[1]==1}
    d2 = { k+"_"+str(c): table[k][:,c].flatten() for k in table.keys() for c in range(0,table[k].shape[1]) if table[k].shape[1]!=1}
    df = pd.DataFrame( {**d2,**d1} )
    df = df.rename(columns={"event_id_0": "run", "event_id_1": "sub", "event_id_2": "evt"})
    return df
