from fc_utils import Tree

def getCourse(courseCatalog, course):
    if courseCatalog.isLeaf():
        if courseCatalog.getValue() == course:
            return course
        else:
            return None
    else:
        for child in courseCatalog.getChildren():
            res = getCourse(child, course)
            if res:
                return courseCatalog.getValue() + "." + res
        return None

def testGetCourse():
    '''
                                          ┌─── 18-100 
                                          │
                              ┌─── ECE ───┼─── 18-202 
                              │           │
               ┌──── CIT ─────┤           └─── 18-213 
               │              │
               │              │           ┌─── 42-101 
               │              └─── BME ───┤
               │                          └─── 42-201 
               │
               │                                         ┌─── 15-110 
    ─── CMU ───┤                          ┌─── Intro ────┤
               │                          │              └─── 15-112 
               │                          │
               ├──── SCS ───────── CS ────┼─── 15-122 
               │                          │
               │                          ├─── 15-150 
               │                          │
               │                          └─── 15-213 
               │
               ├─── 99-307 
               │
               └─── 99-308 
     '''
    courseCatalog = Tree('CMU',
                         Tree('CIT',
                              Tree('ECE',
                                   Tree('18-100'),
                                   Tree('18-202'),
                                   Tree('18-213')
                              ),
                              Tree('BME',
                                   Tree('42-101'),
                                   Tree('42-201')
                              ),
                         ),
                         Tree('SCS',
                              Tree('CS',
                                   Tree('Intro',
                                        Tree('15-110'),
                                        Tree('15-112')
                                   ),
                                   Tree('15-122'),
                                   Tree('15-150'),
                                   Tree('15-213')
                              ),
                         ),
                         Tree('99-307'),
                         Tree('99-308')
                    )
    assert(getCourse(courseCatalog, '18-100') == 'CMU.CIT.ECE.18-100')
    assert(getCourse(courseCatalog, '15-112') == 'CMU.SCS.CS.Intro.15-112')
    assert(getCourse(courseCatalog, '15-213') == 'CMU.SCS.CS.15-213')
    assert(getCourse(courseCatalog, '99-307') == 'CMU.99-307')
    assert(getCourse(courseCatalog, '15-251') == None)

    '''
                         ┌─── 10-100 
                         │
    ─── SA ─────── CB ───┼─── 10-200 
                         │
                         └───── DC ───────── 20-300 
    '''
    courseCatalog = Tree('SA',
                         Tree('CB',
                              Tree('10-100'),
                              Tree('10-200'),
                              Tree('DC',
                                   Tree('20-300')
                                  )
                             )
                        )
    assert(getCourse(courseCatalog, '10-100') == 'SA.CB.10-100')
    assert(getCourse(courseCatalog, '10-200') == 'SA.CB.10-200')
    assert(getCourse(courseCatalog, '20-300') == 'SA.CB.DC.20-300')
    assert(getCourse(courseCatalog, '30-400') == None)

def main():
    testGetCourse()

main()