# pdm-fabric: Fabric command shortcuts for PDM

A plugin that gives you command shortcuts for developing with [PDM](https://pdm.fming.dev/) and
[Fabric](https://www.fabfile.org).


## Requirements

Tested with PDM 2.1.X

## Install

`pdm plugin add pdm-fabric`

## Usage

### fab

Example: `pdm fab shell --env dev`

## Configuring .env

pdm-fabric inherits from the `pdm run` command, so if you would like to load a dotenv file, use the
same notation in your `pyproject.toml` file.

```toml
[tool.pdm.scripts]
_.env_file = ".env"
```

## Thanks to the following projects as the idea came from them not me

https://github.com/neutron-sync/pdm-django

https://github.com/pdm-project/pdm
