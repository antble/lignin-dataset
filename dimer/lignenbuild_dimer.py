from ligningen import LigninBuilder, LigninSequence

# 1. Configuration Data
VALID_MONOMER_TYPES = {"G", "S", "H"} # H/P 

VALID_LINKAGES = {
    "beta-O-4":  "BO4",
    "beta-5":    "B5",
    "beta-beta": "BB",
    "4-O-5":     "4O5",
    "5-5":       "55",
    "alpha-O-4": "AO4",
}

# 2. Logic Check Function
def is_chemically_valid(monomer1, monomer2, linkage):
    """
    Validates if a dimer can physically form based on monomer substitution.
    """
    # Rule: beta-5, 4-O-5, and 5-5 require an open 5-position.
    # S-units have a methoxy group at the 5-position, so they are blocked.
    five_pos_linkages = {"beta-5", "4-O-5", "5-5"}
    
    if linkage in five_pos_linkages:
        if monomer1 == "S" or monomer2 == "S":
            return False
            
    return True

# 3. Generating the Dataset
all_dimers = []

for m1 in sorted(VALID_MONOMER_TYPES):
    for m2 in sorted(VALID_MONOMER_TYPES):
        for link_name in VALID_LINKAGES.keys():
            
            if is_chemically_valid(m1, m2, link_name):
                all_dimers.append((m1, m2, link_name))

# 4. Execution Loop
for seed, target, link in all_dimers:
    try:
        # Initializing the sequence
        seq = LigninSequence()
        seq.add(seed)
        seq.add(target, linkage=link)
        
        print(f"Constructed: {seed} --({link})--> {target}")

        builder = LigninBuilder(work_dir=f"{seed}{target}_{link}")
        builder.generate_topology_sequence(seq)  
        builder.build_lignin()
        builder.run_find_missing_terms() 
        builder.minimize_system(solvated=False)
    except Exception as e:
        print(f"Failed to build {seed}-{link}-{target}: {e}")

print(f"\nTotal valid dimers generated: {len(all_dimers)}")