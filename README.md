# Twitter Service

A system that tracks tweets and replies of these
accounts (alikarimi_ak8,taylorlorenz,cathiedwood) from February 1st, 2023 onwards.

## Installation

Use the docker to install Twitter Service

```bash
docker-compose up
```

## API Usage

To return a json list of all tracked accounts.
```bash
http://82.115.20.139:5100/accounts
```

To Return a json of the user's conversation threads since start.
```bash
http://82.115.20.139:5100/tweets/<user>
```
```bash
http://82.115.20.139:5100/tweets/alikarimi_ak8
```

To return a json of information about the audience for a user's account.
```bash
http://82.115.20.139:5100/audiences/<user>
```
```bash
http://82.115.20.139:5100/audiences/alikarimi_ak8
```

To return a json about the sentiment information of an account (e.g. thread level, audience level)
```bash
http://82.115.20.139:5100/sentiment/<user>/<thread>
```
```bash
http://82.115.20.139:5100/sentiment/GeorgePointon_/1629085362214543361
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
