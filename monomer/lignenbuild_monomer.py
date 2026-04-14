from ligningen import LigninBuilder, LigninSequence


for monomer in ['S','P', 'G']:
    seq = LigninSequence()
    seq.add("G")                        # seed — no linkage
    builder = LigninBuilder(work_dir=f"{monomer}_monomer")
    builder.generate_topology_sequence(seq) 
    builder.build_lignin()
    builder.minimize_system(solvated=False)