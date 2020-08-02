Premier league and NBA backend
==============================

This is the backend API server for retrieving data for matches from the 
premier league and NBA.

Set up
------
To use this server locally it is advised to set up a Python virtual
environment. 

To setup a Python virtual environment:
1. Download project and unpack using `tar -xzf roy_hanley_octopus_test.tar.gz`
2. Change into the project directory: `cd roy_hanley_octopus_test`
3. Run `sudo apt-get install python3-venv` or it's Mac equivalent
4. Run this command to create a virtual environment: `python3 -m venv venv`
5. Activate the virtual environment: `source venv/bin/activate`

Now this is done run `make setup_local`. This will install project
libraries, run migrations and import Premier league and NBA data.

Once `setup_local` has completed run `make server` to view the
API endpoint at `http://localhost:8000/graphql`

Running queries
---------------
You are now ready to run queries. This server uses graphQL. Below are a few
example queries you could try:

To view match data from both the premier league and NBA:
```
query {
    premierLeagueMatches {
    matchDate
    homeTeam {
      name
    }
    homeScore
    awayTeam {
      name
    }
    awayScore
  }
  nbaMatches {
    matchDate
    homeTeam {
      name
    }
    homeScore
    awayTeam {
      name
    }
    awayScore    
  }
}
```

Results are limited to 40 matches per page. The API implements simple 
pagination to view more results. Here is an example:
```
query {
    premierLeagueMatches(page: 2) {
    matchDate
    homeTeam {
      name
    }
    homeScore
    awayTeam {
      name
    }
    awayScore
  }
}
```

You can view less or more match results per page by doing this:
```
query {
    premierLeagueMatches(page: 1, perPage:5) {
    matchDate
    homeTeam {
      name
    }
    homeScore
    awayTeam {
      name
    }
    awayScore
  }
}
```

You can filter matches by date by doing this:
```
query {
    premierLeagueMatches(date: "2019-08-10") {
    matchDate
    homeTeam {
      name
    }
    homeScore
    awayTeam {
      name
    }
    awayScore
  }
}
```
