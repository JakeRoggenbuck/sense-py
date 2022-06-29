import lang
import git


def main():
    language = lang.get_lang("./")
    print(language)

    has_git_dir = git.has_git("./")
    if has_git_dir:
        print("Is git!")
    else:
        print("Is not git.")

    local = git.is_local_git("./")
    if local:
        print("Is local!")
    else:
        print("Is not local.")


if __name__ == "__main__":
    main()
