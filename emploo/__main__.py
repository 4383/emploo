import argparse
import json
import textwrap

import requests


def argparser():
    parser = argparse.ArgumentParser(
        description="Collect company employees profiles from linkedin. \
                    Can be used during your OSINT investigation"
    )
    subparsers = parser.add_subparsers(help="Available commands", dest="subparser_name")
    parser_init = subparsers.add_parser("init", help="Init your system")
    parser_search = subparsers.add_parser("search", help="Search company employees")
    parser_search.add_argument("company", type=str, help="Company name to investigate")
    parser_search.add_argument(
        "-i",
        "--google-id",
        type=str,
        default=None,
        help="Your google GPSE id. \
              If you already stored your id in the config, passing \
              this argument will override your local config.",
    )
    parser_search.add_argument(
        "-k",
        "--google-key",
        default=None,
        help="Your google api key. \
              if you already stored your id in the config, passing \
              this argument will override your local config.",
    )
    parser_search.add_argument(
        "-o",
        "--output-file",
        default=None,
        help="Save results in the specified output file. \
              If this option is not given, the results will \
              displayed in the stdout.",
    )
    return parser.parse_args()


def init():
    return textwrap.dedent(
        """
        <Annotations>
          <Annotation about="www.linkedin.com/in/*" timestamp="0x00018c12afac40" score="1.0">
            <Label name="_include_"/>
            <AdditionalData attribute="original_url" value="www.linkedin.com/in/*"/>
          </Annotation>
        </Annotations>
    """
    )


def search(args):
    url = "https://www.googleapis.com/customsearch/v1"
    payload = {
        "q": args.company,
        "key": args.google_key,
        "cx": args.google_id,
        "start": 0,
    }

    profiles = []
    rounds = 1
    while True:
        r = requests.get(url, params=payload)
        if r.status_code != 200:
            print(f"error: {r.status_code}")
            print(r.url)
            print(r.text)
            print(payload)
            return

        data = r.json()
        profiles.extend(data["items"])
        print(f"{rounds} - {len(profiles)} collect profiles...")
        rounds += 1
        if data["queries"].get("nextPage", None):
            payload["start"] = data["queries"]["nextPage"][0]["startIndex"]
            if payload["start"] > 100:
                print("Google API limitation reached (100 results).")
                print("Aborting")
                break
        else:
            break

    output = args.output_file
    if output:
        with open(output, "w+") as f:
            f.write(json.dumps(profiles, indent=4))
            print(f"results saved into: {output}")
    else:
        print(profiles)


def main():
    args = argparser()
    if args.subparser_name == "init":
        print(init())
    elif args.subparser_name == "search":
        search(args)


if __name__ == "__main__":
    main()
