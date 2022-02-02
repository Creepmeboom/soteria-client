# Project Soteria

A Bot for Discord in Python, hosted in the PrivateCraft-Network

## Features

### Security related Features

- Deletes Messages with executable files attached or linked to it, immediatly and returns a Warning
- Deletes Messages with Links to Websites, known to be phishing-Sites which try to grab account-data to be used for hacking, immediatly and returns a Warning
- Deletes Messages where X or more Users get pinged individually (default is 5, this is set globally), servermutes the Author in all Textchannels using a dedicated Serverrole and returns a Warning. This Operation will just ping the Serverowner with a warning if no Muterole is set!
  - ToDo: pinging a set Moderator-Role instead of the Owner
- A per-server Blacklist with forbidden phrases to filter Textmessages
  - Coming Soon: An intelligent System (Codename: BDS) which detects iterations and alterations of blacklisted words
- A Strikesystem against users, disobeying f.e. the Blacklist or the "no-executables"-rule
  - Strikes can be adjusted manually per user
  - Once a user reaches maximum strikes level (set per server, default is 3) an action will get executed on that user. this can be:
    - Servermute/deaf in Textchannels or all Channels
    - Temp-/Timeban or permanent ban
    - Timeout
    - custom Action (soon TM)
  - Striked Messages get deleted from the server, logged in Soterias internal per-server Messagecache and logged in Soterias internal per-server Usercache, all of those contain the Original Message ID, Timestamp of Deletion, origin channel and latest content.
- Access to the Bot is handled in 4/5 Layers/levels
  - Level 0: Command:Forbidden -> The Author of the Command could have been a higher level, but the Message with the Command got sorted out becuse it contained a globally forbidden phrase, which triggered the anti-scam-detection. The Command will be logged whatsoever!
  - Level 0: Command:Unauthorized -> The Author of the Command is not authorized, leaving the command unexecuted. The Command will be logged whatsoever!
  - Level 1: Command:Role -> The Author inherits a role, that is setup as authorized for Soterias Commands. The Command will be executed!
  - Level 2: Command:Owner -> The Author is the Current Owner of the Server. The Command will be executed!
    - _Note: Once the Ownership is transfered, someone authorized needs to update Soterias Servercache, so the new Owner will be acknowledged as one!_
  - Level 3: Command:Master -> The Author is me, the Creator for Soteria. The Command will be executed! (Used to limit access to debuggingcommands to myself, since those commands can change Soterias behavior on a Systemlevel!)

### Discord Servermoderation Features

- The Standard Purge Command
- Profiles with different Roles to bulk-add/-remove Roles from one or more Users in one command.
- Mute/Unmute User manually

### Data related Features (most of them required to operate)

- Logging all Textchannels history live on read (the history before Soteria came can be read manually via command)
- Logging (optionally notifying) when a User changes his Visibility
- Logging when someone changes his Nickname and who changed the Nickname
- Logging when someone starts typing, including the channel of the event
- Logging Messages, when they get deleted (optionally posting their content to their original place)
- Logging commands sent to Soteria, including Origin, Author and Accesslevel (won't work cross-server)

### Community Features

- Broadcast Messages from a Source Textchannel to Destination Textchannels on other Servers
- Ban people from one server and sync their banlist with other Servers
- 2FA to group Servers to one "Alliance", to use the other Community Features, mentioned above. For that, an Administrator of the Alliance's Masterserver has to work with the new Members Serverowner together to establish the Link within Soteria
- Writing Pings for Events using TeamUp. Which Roles need to be pinged for what type of event can be adjusted
