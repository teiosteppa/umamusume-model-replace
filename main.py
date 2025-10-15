import umaModelReplace

uma = umaModelReplace.UmaReplace()


def replace_char_body_texture(char_id: str):
    is_not_exist, msg = uma.save_char_body_texture(char_id, False)
    if not is_not_exist:
        print(f"Unpacked resources already exist: {msg}")
        do_replace = input('Enter "Y" to overwrite unpacked resources, or enter anything else to skip export: ')
        if do_replace in ["Y", "y"]:
            _, msg = uma.save_char_body_texture(char_id, True)

    print(f"Resource export attempted. Please check the directory: {msg}")
    do_fin = input(
        'Please modify/replace the files. When finished, enter "Y" to repackage and replace the game files.\n'
        'If you don’t want to modify now, enter anything else to exit. Next time you can choose "skip export".\n'
        "Input: "
    )
    if do_fin.strip() in ["Y", "y"]:
        uma.replace_char_body_texture(char_id)
        print("Texture has been modified")


def replace_char_head_texture(char_id: str):
    for n, i in enumerate(uma.save_char_head_texture(char_id, False)):
        is_not_exist, msg = i

        if not is_not_exist:
            print(f"Unpacked resources already exist: {msg}")
            do_replace = input('Enter "Y" to overwrite unpacked resources, or enter anything else to skip export: ')
            if do_replace in ["Y", "y"]:
                _, msg = uma.save_char_head_texture(char_id, True, n)[0]

        print(f"Resource export attempted. Please check the directory: {msg}")

    do_fin = input(
        'Please modify/replace the files. When finished, enter "Y" to repackage and replace the game files.\n'
        'If you don’t want to modify now, enter anything else to exit. Next time you can choose "skip export".\n'
        "Input: "
    )
    if do_fin.strip() in ["Y", "y"]:
        uma.replace_char_head_texture(char_id)
        print("Texture has been modified")


if __name__ == "__main__":
    while True:
        do_type = input(
            "[1] Replace head model\n"
            "[2] Replace body model\n"
            "[3] Replace tail model (not recommended)\n"
            "[4] Replace head and body models\n"
            "[5] Modify character body texture\n"
            "[6] Replace gacha opening character\n"
            "[7] Replace skill animation\n"
            "[8] Replace G1 victory animation (experimental)\n"
            "[9] Unlock Live outfits\n"
            "[10] Clear all Live blur effects\n"
            "[11] Modify character head texture\n"
            "[98] Restore all modifications\n"
            "[99] Exit\n"
            "Please select an option: "
        )

        if do_type == "1":
            print("Please enter a 7-character ID, e.g., 1046_01")
            uma.replace_head(input("Source ID: "), input("Target ID: "))
            print("Replacement complete")

        if do_type == "2":
            print("Please enter a 7-character ID, e.g., 1046_01")
            uma.replace_body(input("Source ID: "), input("Target ID: "))
            print("Replacement complete")

        if do_type == "3":
            checkDo = input(
                "Note: Currently you cannot replace tails across different models. "
                "The target character cannot appear at the same time as the original character.\n"
                "If you still want to proceed, enter y to continue: "
            )
            if checkDo not in ["y", "Y"]:
                continue
            print("Please enter a 4-digit ID, e.g., 1046")
            uma.replace_tail(input("Source ID: "), input("Target ID: "))
            print("Replacement complete")

        if do_type == "4":
            print("Please enter a 7-character ID, e.g., 1046_01")
            inId1 = input("Source ID: ")
            inId2 = input("Target ID: ")
            uma.replace_head(inId1, inId2)
            uma.replace_body(inId1, inId2)
            print("Replacement complete")

        if do_type == "5":
            print("Please enter a 7-character ID, e.g., 1046_01")
            replace_char_body_texture(input("Character 7-character ID: "))

        if do_type == "6":
            print("Please enter the 6-digit outfit ID for the regular gacha opening animation, e.g., 100101 or 100130")
            uma.edit_gac_chr_start(input("Outfit 6-digit ID: "), '001')
            print("Please enter the 6-digit outfit ID for the chairman gacha opening animation, e.g., 100101 or 100130")
            uma.edit_gac_chr_start(input("Outfit 6-digit ID: "), '002')
            print("Replacement complete")

        if do_type == "7":
            print("Please enter the 6-digit character skill ID, e.g., 100101 or 100102")
            uma.edit_cutin_skill(input("Source ID: "), input("Target ID: "))

        if do_type == "8":
            checkDo = input(
                "Note: Some victory animations may cause audio glitches or black screens after replacement.\n"
                "If you still want to proceed, enter y to continue: "
            )
            if checkDo not in ["y", "Y"]:
                continue
            print("Please enter the 6-digit victory animation ID, e.g., 100101 or 100102")
            uma.replace_race_result(input("Source ID: "), input("Target ID: "))
            print("Replacement complete")

        if do_type == "9":
            uma.unlock_live_dress()
            print("Unlock complete")

        if do_type == "10":
            edit_live_id = input("Live ID (usually 4 digits; leave blank to modify all): ").strip()
            uma.clear_live_blur(edit_live_id)
            # Tip: This works best paired with the TLG plugin's Live free camera feature.
            # Repo: https://github.com/MinamiChiwa/Trainers-Legend-G

        if do_type == "11":
            print("Please enter a 7-character ID, e.g., 1046_01")
            replace_char_head_texture(input("Character 7-character ID: "))

        if do_type == "98":
            uma.file_restore()
            print("Modifications restored")

        if do_type == "99":
            break

        input("Press enter to continue...\n")
