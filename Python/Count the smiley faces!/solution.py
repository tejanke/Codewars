def count_smileys(arr):
    eyes = [
        ":",
        ";"
    ]
    noses = [
        "-",
        "~"
    ]
    mouthes = [
        ")",
        "D"
    ]
    if arr == "":
        return 0
    else:
        result = 0
        for face in arr:
            if len(face) < 2:
                return 0
            if len(face) == 2:
                for eye in eyes:
                    if eye in face:
                        for mouth in mouthes:
                            if mouth in face:
                                result += 1
            if len(face) == 3:
                for eye in eyes:
                    if eye in face:
                        for nose in noses:
                            if nose in face:
                                for mouth in mouthes:
                                    if mouth in face:
                                        result += 1
    return result
