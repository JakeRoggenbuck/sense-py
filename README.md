# sense-py
Sense the directories around you, are they git repositories, what language, etc.

## Languages
[ :snake: sense-py](https://github.com/JakeRoggenbuck/sense-py) || [:crab: sense-rs](https://github.com/JakeRoggenbuck/sense-rs) || 
[:hamster: sense-go](https://github.com/JakeRoggenbuck/sense-go) || [🇨 sense-c](https://github.com/JakeRoggenbuck/sense-c) || [🔥 sense-cpp](https://github.com/JakeRoggenbuck/sense-cpp)

## Why?
#### Why so many langs?
Because I write projects pretty regularly in all of these languages and want a consistent API and available library support for all of them.

## API

### Git

```py
has_git(path: str) -> bool
is_local_git(path: str) -> bool
```

### Language
```py
get_lang(path: str) -> Lang
```

## Example
```c
# todo
```

## Supported langs
- [x] Python
- [x] JavaScript
- [x] Rust
- [x] Java
- [x] Go
- [ ] TypeScript
- [ ] C
- [ ] CPP

## Contributing
If you would like to add features or language support, that would be amazing!
