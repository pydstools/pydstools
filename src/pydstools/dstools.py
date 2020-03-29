# -*- coding: utf-8 -*-
'''
Created on Wed Sep  9 13:26:08 2015

@author: jmmauricio
'''



def obj2dic(app):
    '''
    Input
    =====

    Application instance

    Output
    ======

    Diccionary with the elements

    '''

    dsls = app.GetCalcRelevantObjects("*.ElmDsl")
    name2dsl = {}
    for dsl in dsls:
        parent = dsl.GetParent()
        parent_name = parent.cDisplayName
        dsl_name = dsl.cDisplayName
        if not parent_name in name2dsl:
            name2dsl.update({parent_name:{}})
        name2dsl[parent_name].update({dsl_name:dsl})

    syms = app.GetCalcRelevantObjects("*.ElmSym")
    name2sym = {}
    for sym in syms:
        name2sym.update({sym.cDisplayName:sym})

    trafos = app.GetCalcRelevantObjects("*.ElmTr2")
    name2tr2 = {}
    for trafo in trafos:
        name2tr2.update({trafo.cDisplayName:trafo})


    loads = app.GetCalcRelevantObjects("*.ElmLod")
    name2load = {}
    for load in loads:                       
        name2load.update({load.cDisplayName:load})   

    genstats = app.GetCalcRelevantObjects("*.ElmGenstat")
    name2genstat = {}
    for genstat in genstats:                       
        name2genstat.update({genstat.cDisplayName:genstat})        

    buses = app.GetCalcRelevantObjects("*.ElmTerm")
    name2bus = {}
    for bus in buses:
        name2bus.update({bus.cDisplayName:bus})  
    print(name2bus)

    shunts = app.GetCalcRelevantObjects("*.ElmShnt")
    name2shnt = {}
    for shunt in shunts:                       
        name2shnt.update({shunt.cDisplayName:shunt})        

    lines = app.GetCalcRelevantObjects("*.ElmLne") 
    name2lne = {}
    for line in lines:                       
        name2lne.update({line.cDisplayName:line})    

    name2elm = {'bus':name2bus,'sym':name2sym,'load':name2load,'genstat':name2genstat,
                'dsl':name2dsl, 'tr2':name2tr2, 'shnt':name2shnt, 'lne':name2lne}

    return name2elm