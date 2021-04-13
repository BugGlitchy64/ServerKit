# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project hasn't adhere to [Semantic Versioning](https://semver.org/spec/v2.0.0.html) yet. (will be in Version Alpha 4.0.0!)

## [Unreleased]

## [Alpha 0.3.5.1] - 2021-04-12
### Fixed
- One line in Music command (wait(1)) caused "This interaction failed" message but plays music while using /play.

## Alpha 0.3.5 - 2021-04-12
### Changed
- Specify that Spotify links works with play command.

### Fixed
- Fix for "This interaction failed" message while using slash commands.

## Alpha 0.3.4 - 2021-04-11
### Fixed
- Fix for an extra ) in the Ban command.

## Alpha 0.3.3 - 2021-04-11
### Fixed
- Fix slash command options because of me forgot to import `create_option`.

## Alpha 0.3.2 - 2021-04-11
### Changed
- Include option explainations into slash commands.

### Fixed
- Update pulling reason text from user's message to prevent error.

## Alpha 0.3.1 - 2021-04-11
### Changed
- Includes slash command in help command and bot's status.

### Fixed
- Fixed moderation command due to a misnaming in the async functions.

## Alpha 0.3 - 2021-04-11
### Added
- Slash command support.
- @someone command added. (throwback to Discord April Fools 2018)

### Changed
- Update invite link to support slash command and replace Administrstor permission with the required ones.

### Deprecated
- Move the contents of changelog and info command to Github and Help command respectively, command still exists.

### Fixed
- Fixed embed not showing up in play, stop, pause commands while user isn't in a voice channel.
- Attempting to fix 403 Error command
- Removed useless options in youtube-dl

## Alpha 0.2.3 - 2021-04-09
### Added
- More fun commands (Eightball, dice)
- Moderation commands (Ban, Kick)

### Changed
- Moved many commands into a cog. (info, changelog, help and ping are in info cog)

## Alpha 0.2.2 - 2021-04-08?
### Changed
- New branding change.

### Fixed
- Bug fixes.

## Alpha 0.2.1 - 2021-04-08?
### Fixed
- Bug fixes.

## Alpha 0.2 - 2021-04-08?
### Added
- Music commands (join, leave, play, pause, stop)
- Changelog command

### Fixed
- Bug Fixes

## Alpha 0.1.1.4 - 2021-04-07?
### Fixed
- Bug Fixes

[Unreleased]:
https://github.com/BugGlitchy64/ServerKit/compare/v0.3.5.1-alpha...HEAD
[Alpha 0.3.5.1]:
https://github.com/BugGlitchy64/ServerKit/releases/tag/v0.3.5.1-alpha
