import pandas as pd

#def Table2DataFrame(table):
#    d1 = { k: table[k][:].flatten() for k in table.keys() if table[k].shape[1]==1}
#    d2 = { k+"_"+str(c): table[k][:,c].flatten() for k in table.keys() for c in range(0,table[k].shape[1]) if table[k].shape[1]!=1}
#    df = pd.DataFrame( {**d2,**d1} )
#    df = df.rename(columns={"event_id_0": "run", "event_id_1": "sub", "event_id_2": "evt"})
#    return df

def Table2DataFrame(file,table_name,first_evt_idx,total_evts,dict_rename={}):
    #
    table = file[table_name]
    df = pd.DataFrame(table["event_id"],columns=["run","subrun","event"])
    df['count'] = 0
    df = df.reset_index().rename(columns={'index':'orig_index'})
    #group by event id
    tmp = df.groupby(['run','subrun','event'])
    #count entries per event
    res = tmp.agg({'count': 'count', 'orig_index': lambda x: tuple(x)}).sort_values(by='orig_index').reset_index()
    #assign unique id per event
    res['evt_idx'] = (tmp.cumcount()==0).astype(int)
    res['evt_idx'] = res['evt_idx'].cumsum()-1
    #find rowas corresponding to event range
    ifirst = res['count'][0:first_evt_idx].sum()
    itotal = res['count'][first_evt_idx:first_evt_idx+total_evts].sum()
    # make data frame
    d1 = { k: table[k][ifirst:ifirst+itotal].flatten() for k in table.keys() if table[k].shape[1]==1}
    d2 = { k+"_"+str(c): table[k][ifirst:ifirst+itotal,c].flatten() for k in table.keys() for c in range(0,table[k].shape[1]) if table[k].shape[1]!=1}
    d3 = { 'evt_idx': res['evt_idx'][ifirst:ifirst+itotal]}
    #build data frame
    df = pd.DataFrame( {**d3,**d2,**d1} )
    #rename and drop columns
    df = df.rename(columns={"event_id_0": "run", "event_id_1": "subrun", "event_id_2": "event"})
    if table_name!="event": df = df.drop(columns=["run","subrun","event"])
    for key, value in dict_rename.items():
        df = df.rename(columns={ key+"_"+str(v): value[v] for v in range(0,len(value))})
    return df

#def EventMask(df,evt):
#    return (df[["run","sub","evt"]].to_numpy() == evt).all(axis=1)
