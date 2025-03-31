from data_structures.test_verion import TestVersion


def get_two_versions(struct_list):
    v1_structs = [v1_struct for v1_struct in struct_list if v1_struct.version == TestVersion.V1]
    v2_structs = [v2_struct for v2_struct in struct_list if v2_struct.version == TestVersion.V2]

    if len(v1_structs) != 1 or len(v2_structs) != 1:
        print("Error: Expected exactly one opt and one org file")
        return

    return v1_structs[0], v2_structs[0] # Handling comparison of two tests only