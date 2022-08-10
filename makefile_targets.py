# For the full list of possible targets,
# see the Makefile, particularly the definition of .PHONY.
targets = [
  "show_config",
  "show_params",
  # "tests",
    # On this branch (aws-ubuntu),
    # it would not make sense to run the tests.
    # They are only useful to the developer, not the user.
    # Moreover many of them should fail under user-supplied conditions
    # different from the baseline.
  "reports",
]
