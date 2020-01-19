## Task 1

Write a microservice which exposes an HTTP endpoint to accept a bid for a competition and return
the status of that bid in the response. In this competition the lowest bid wins but should not
see details of any other bid.

- The competition will be uniquely identified by a hashid.
- The response should indicate whether the bid was the lowest so far or not.

## Task 2

Enable competitions to be closed at a set date and time. If any bids are submitted once the
competition is closed they should be refused.

## Provisioning

Provide repeatable steps (with instructions) to install all requirements and be able to run any tests or commands. Ideally the
solution would work on any platform e.g. Docker.

# Solutions

## Instructions

```
$ docker build -t bid_competition:latest .
$ docker run -d -p 5000:5000 bid_competition:latest
$ localhost:5000/bids_date/ADJCKDSJC/<any_number>
"Submission too late. The competition expiry date has passed."

# For a submission on time:
$ localhost:5000/bids_date/LAPLCKDSJL/9
"winner so far"

$ localhost:5000/bids_date/LAPLCKDSJL/98
"loser"

$ localhost:5000/bids_date/LAPLCKDSJL/7
"winner so far"

$ localhost:5000/bids_date/LAPLCKDSJL/9
"loser"

```

Clean up:
docker ps
docker kill <CONTAINER ID>

## Task 1

The only existing endpoint in task one is `bids`, which only checks for the minimum bid entered in the competition so far.

## Task 2

For task 2, I created a new endpoint `bids_date`, which checks on whether a submission is made on time. So, I added a date fiels in the competitions dictionary, which represents the time by which submissions are still accepted. For simplicity, I created 2 competitions, one with an expiry date tomorrow at this time (whose id is: `LAPLCKDSJL`) and another one with expiry date yesterday at this time (whose id is: `ADJCKDSJC`).
