# pattern_matching_bc.py

from __future__ import with_statement
import itertools
from pyke import contexts, pattern, bc_rule

pyke_version = '1.1.1'
compiler_version = 1

def knows_pattern_matching(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(itertools.imap(lambda pat, arg:
                              pat.match_pattern(context, context,
                                                arg, arg_context),
                            patterns,
                            arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        engine.get_ke('questions', 'pat_master').reset()
        with engine.prove(rule.rule_base.root_name, 'knows_pat_master', context,
                          ()) \
          as gen_2:
          for x_2 in gen_2:
            assert x_2 is None, \
              "pattern_matching.knows_pattern_matching: got unexpected plan from when clause 2"
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def knows_pattern_matching_2(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(itertools.imap(lambda pat, arg:
                              pat.match_pattern(context, context,
                                                arg, arg_context),
                            patterns,
                            arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove(rule.rule_base.root_name, 'learned_pattern_matching', context,
                          ()) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "pattern_matching.knows_pattern_matching_2: got unexpected plan from when clause 1"
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def knows_pat_master(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(itertools.imap(lambda pat, arg:
                              pat.match_pattern(context, context,
                                                arg, arg_context),
                            patterns,
                            arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'pat_master', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "pattern_matching.knows_pat_master: got unexpected plan from when clause 1"
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def learned_pattern_matching(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(itertools.imap(lambda pat, arg:
                              pat.match_pattern(context, context,
                                                arg, arg_context),
                            patterns,
                            arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove(rule.rule_base.root_name, 'taught_pattern_matching', context,
                          ()) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "pattern_matching.learned_pattern_matching: got unexpected plan from when clause 1"
            with engine.prove(rule.rule_base.root_name, 'knows_pattern_matching', context,
                              ()) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "pattern_matching.learned_pattern_matching: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def taught_pattern_matching_1_2_4_16(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(itertools.imap(lambda pat, arg:
                              pat.match_pattern(context, context,
                                                arg, arg_context),
                            patterns,
                            arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'pat_master', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "pattern_matching.taught_pattern_matching_1_2_4_16: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (1, 2, 4, 16):
              with engine.prove(rule.rule_base.root_name, 'knows_pattern_variable_syntax', context,
                                ()) \
                as gen_3:
                for x_3 in gen_3:
                  assert x_3 is None, \
                    "pattern_matching.taught_pattern_matching_1_2_4_16: got unexpected plan from when clause 3"
                  with engine.prove(rule.rule_base.root_name, 'knows_patterns', context,
                                    ()) \
                    as gen_4:
                    for x_4 in gen_4:
                      assert x_4 is None, \
                        "pattern_matching.taught_pattern_matching_1_2_4_16: got unexpected plan from when clause 4"
                      with engine.prove(rule.rule_base.root_name, 'knows_how_patterns_match', context,
                                        ()) \
                        as gen_5:
                        for x_5 in gen_5:
                          assert x_5 is None, \
                            "pattern_matching.taught_pattern_matching_1_2_4_16: got unexpected plan from when clause 5"
                          with engine.prove(rule.rule_base.root_name, 'knows_pattern_variable_scope', context,
                                            ()) \
                            as gen_6:
                            for x_6 in gen_6:
                              assert x_6 is None, \
                                "pattern_matching.taught_pattern_matching_1_2_4_16: got unexpected plan from when clause 6"
                              rule.rule_base.num_bc_rule_successes += 1
                              yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def taught_pattern_matching_3_5_6_9_15(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(itertools.imap(lambda pat, arg:
                              pat.match_pattern(context, context,
                                                arg, arg_context),
                            patterns,
                            arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'pat_master', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "pattern_matching.taught_pattern_matching_3_5_6_9_15: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (3, 5, 6, 9, 15):
              with engine.prove(rule.rule_base.root_name, 'knows_tuple_patterns', context,
                                ()) \
                as gen_3:
                for x_3 in gen_3:
                  assert x_3 is None, \
                    "pattern_matching.taught_pattern_matching_3_5_6_9_15: got unexpected plan from when clause 3"
                  rule.rule_base.num_bc_rule_successes += 1
                  yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def taught_pattern_matching_7_8_10(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(itertools.imap(lambda pat, arg:
                              pat.match_pattern(context, context,
                                                arg, arg_context),
                            patterns,
                            arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'pat_master', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "pattern_matching.taught_pattern_matching_7_8_10: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (7, 8, 10):
              with engine.prove(rule.rule_base.root_name, 'knows_rest_variable', context,
                                ()) \
                as gen_3:
                for x_3 in gen_3:
                  assert x_3 is None, \
                    "pattern_matching.taught_pattern_matching_7_8_10: got unexpected plan from when clause 3"
                  rule.rule_base.num_bc_rule_successes += 1
                  yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def taught_pattern_matching_11_12(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(itertools.imap(lambda pat, arg:
                              pat.match_pattern(context, context,
                                                arg, arg_context),
                            patterns,
                            arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'pat_master', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "pattern_matching.taught_pattern_matching_11_12: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (11, 12):
              with engine.prove(rule.rule_base.root_name, 'knows_pattern_variable_scope', context,
                                ()) \
                as gen_3:
                for x_3 in gen_3:
                  assert x_3 is None, \
                    "pattern_matching.taught_pattern_matching_11_12: got unexpected plan from when clause 3"
                  rule.rule_base.num_bc_rule_successes += 1
                  yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def taught_pattern_matching_14(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(itertools.imap(lambda pat, arg:
                              pat.match_pattern(context, context,
                                                arg, arg_context),
                            patterns,
                            arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'pat_master', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "pattern_matching.taught_pattern_matching_14: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (14,):
              with engine.prove(rule.rule_base.root_name, 'knows_how_patterns_match', context,
                                ()) \
                as gen_3:
                for x_3 in gen_3:
                  assert x_3 is None, \
                    "pattern_matching.taught_pattern_matching_14: got unexpected plan from when clause 3"
                  with engine.prove(rule.rule_base.root_name, 'knows_pattern_variable_scope', context,
                                    ()) \
                    as gen_4:
                    for x_4 in gen_4:
                      assert x_4 is None, \
                        "pattern_matching.taught_pattern_matching_14: got unexpected plan from when clause 4"
                      rule.rule_base.num_bc_rule_successes += 1
                      yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def knows_pattern_variable_syntax(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(itertools.imap(lambda pat, arg:
                              pat.match_pattern(context, context,
                                                arg, arg_context),
                            patterns,
                            arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'pat_var_syntax', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "pattern_matching.knows_pattern_variable_syntax: got unexpected plan from when clause 1"
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def reset_if_wrong__right(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(itertools.imap(lambda pat, arg:
                              pat.match_pattern(context, context,
                                                arg, arg_context),
                            patterns,
                            arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('special', 'claim_goal', context,
                          ()) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "pattern_matching.reset_if_wrong__right: got unexpected plan from when clause 1"
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def reset_if_wrong__wrong(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(itertools.imap(lambda pat, arg:
                              pat.match_pattern(context, context,
                                                arg, arg_context),
                            patterns,
                            arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        engine.get_ke('questions', context.lookup_data('question')).reset()
        rule.rule_base.num_bc_rule_successes += 1
        yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def knows_patterns(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(itertools.imap(lambda pat, arg:
                              pat.match_pattern(context, context,
                                                arg, arg_context),
                            patterns,
                            arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove(rule.rule_base.root_name, 'knows_literal_patterns', context,
                          ()) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "pattern_matching.knows_patterns: got unexpected plan from when clause 1"
            with engine.prove(rule.rule_base.root_name, 'knows_pattern_variables', context,
                              ()) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "pattern_matching.knows_patterns: got unexpected plan from when clause 2"
                with engine.prove(rule.rule_base.root_name, 'knows_tuple_patterns', context,
                                  ()) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "pattern_matching.knows_patterns: got unexpected plan from when clause 3"
                    rule.rule_base.num_bc_rule_successes += 1
                    yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def knows_literal_patterns(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(itertools.imap(lambda pat, arg:
                              pat.match_pattern(context, context,
                                                arg, arg_context),
                            patterns,
                            arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove(rule.rule_base.root_name, 'ask_until_correct', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "pattern_matching.knows_literal_patterns: got unexpected plan from when clause 1"
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def ask_until_correct__ask(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(itertools.imap(lambda pat, arg:
                              pat.match_pattern(context, context,
                                                arg, arg_context),
                            patterns,
                            arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', context.lookup_data('question'), context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "pattern_matching.ask_until_correct__ask: got unexpected plan from when clause 1"
            with engine.prove('special', 'claim_goal', context,
                              ()) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "pattern_matching.ask_until_correct__ask: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def ask_until_correct__try_again(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(itertools.imap(lambda pat, arg:
                              pat.match_pattern(context, context,
                                                arg, arg_context),
                            patterns,
                            arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        engine.get_ke('questions', context.lookup_data('question')).reset()
        print "Try again:"
        with engine.prove(rule.rule_base.root_name, 'ask_until_correct', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_3:
          for x_3 in gen_3:
            assert x_3 is None, \
              "pattern_matching.ask_until_correct__try_again: got unexpected plan from when clause 3"
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def knows_pattern_variables(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(itertools.imap(lambda pat, arg:
                              pat.match_pattern(context, context,
                                                arg, arg_context),
                            patterns,
                            arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove(rule.rule_base.root_name, 'knows_pattern_variable_syntax', context,
                          ()) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "pattern_matching.knows_pattern_variables: got unexpected plan from when clause 1"
            with engine.prove(rule.rule_base.root_name, 'knows_pattern_variable_scope', context,
                              ()) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "pattern_matching.knows_pattern_variables: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def knows_pattern_variable_scope(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(itertools.imap(lambda pat, arg:
                              pat.match_pattern(context, context,
                                                arg, arg_context),
                            patterns,
                            arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove(rule.rule_base.root_name, 'ask_until_correct', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "pattern_matching.knows_pattern_variable_scope: got unexpected plan from when clause 1"
            with engine.prove('questions', 'anonymous_syntax', context,
                              (rule.pattern(2),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "pattern_matching.knows_pattern_variable_scope: got unexpected plan from when clause 2"
                with engine.prove(rule.rule_base.root_name, 'ask_until_correct', context,
                                  (rule.pattern(3),
                                   rule.pattern(4),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "pattern_matching.knows_pattern_variable_scope: got unexpected plan from when clause 3"
                    rule.rule_base.num_bc_rule_successes += 1
                    yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def knows_how_patterns_match(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(itertools.imap(lambda pat, arg:
                              pat.match_pattern(context, context,
                                                arg, arg_context),
                            patterns,
                            arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'pattern_scope', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "pattern_matching.knows_how_patterns_match: got unexpected plan from when clause 1"
            with engine.prove(rule.rule_base.root_name, 'post_process_pattern_scope', context,
                              (rule.pattern(0),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "pattern_matching.knows_how_patterns_match: got unexpected plan from when clause 2"
                with engine.prove(rule.rule_base.root_name, 'ask_until_correct', context,
                                  (rule.pattern(1),
                                   rule.pattern(2),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "pattern_matching.knows_how_patterns_match: got unexpected plan from when clause 3"
                    rule.rule_base.num_bc_rule_successes += 1
                    yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def post_process_pattern_scope_1(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(itertools.imap(lambda pat, arg:
                              pat.match_pattern(context, context,
                                                arg, arg_context),
                            patterns,
                            arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove(rule.rule_base.root_name, 'knows_literal_patterns', context,
                          ()) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "pattern_matching.post_process_pattern_scope_1: got unexpected plan from when clause 1"
            with engine.prove(rule.rule_base.root_name, 'knows_pattern_variable_syntax', context,
                              ()) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "pattern_matching.post_process_pattern_scope_1: got unexpected plan from when clause 2"
                engine.get_ke('questions', 'pattern_scope').reset()
                with engine.prove(rule.rule_base.root_name, 'knows_how_patterns_match', context,
                                  ()) \
                  as gen_4:
                  for x_4 in gen_4:
                    assert x_4 is None, \
                      "pattern_matching.post_process_pattern_scope_1: got unexpected plan from when clause 4"
                    rule.rule_base.num_bc_rule_successes += 1
                    yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def post_process_pattern_scope_2(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(itertools.imap(lambda pat, arg:
                              pat.match_pattern(context, context,
                                                arg, arg_context),
                            patterns,
                            arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove(rule.rule_base.root_name, 'knows_pattern_variable_scope', context,
                          ()) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "pattern_matching.post_process_pattern_scope_2: got unexpected plan from when clause 1"
            engine.get_ke('questions', 'pattern_scope').reset()
            with engine.prove(rule.rule_base.root_name, 'knows_how_patterns_match', context,
                              ()) \
              as gen_3:
              for x_3 in gen_3:
                assert x_3 is None, \
                  "pattern_matching.post_process_pattern_scope_2: got unexpected plan from when clause 3"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def post_process_pattern_scope_3(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(itertools.imap(lambda pat, arg:
                              pat.match_pattern(context, context,
                                                arg, arg_context),
                            patterns,
                            arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        rule.rule_base.num_bc_rule_successes += 1
        yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def post_process_pattern_scope_4(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(itertools.imap(lambda pat, arg:
                              pat.match_pattern(context, context,
                                                arg, arg_context),
                            patterns,
                            arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove(rule.rule_base.root_name, 'knows_pattern_variable_scope', context,
                          ()) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "pattern_matching.post_process_pattern_scope_4: got unexpected plan from when clause 1"
            with engine.prove('questions', 'same_var_different_rules', context,
                              (rule.pattern(0),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "pattern_matching.post_process_pattern_scope_4: got unexpected plan from when clause 2"
                engine.get_ke('questions', 'pattern_scope').reset()
                with engine.prove(rule.rule_base.root_name, 'knows_how_patterns_match', context,
                                  ()) \
                  as gen_4:
                  for x_4 in gen_4:
                    assert x_4 is None, \
                      "pattern_matching.post_process_pattern_scope_4: got unexpected plan from when clause 4"
                    rule.rule_base.num_bc_rule_successes += 1
                    yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def post_process_pattern_scope_5(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(itertools.imap(lambda pat, arg:
                              pat.match_pattern(context, context,
                                                arg, arg_context),
                            patterns,
                            arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'same_var_different_rules', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "pattern_matching.post_process_pattern_scope_5: got unexpected plan from when clause 1"
            engine.get_ke('questions', 'pattern_scope').reset()
            with engine.prove(rule.rule_base.root_name, 'knows_how_patterns_match', context,
                              ()) \
              as gen_3:
              for x_3 in gen_3:
                assert x_3 is None, \
                  "pattern_matching.post_process_pattern_scope_5: got unexpected plan from when clause 3"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def post_process_pattern_scope_6(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(itertools.imap(lambda pat, arg:
                              pat.match_pattern(context, context,
                                                arg, arg_context),
                            patterns,
                            arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove(rule.rule_base.root_name, 'knows_patterns', context,
                          ()) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "pattern_matching.post_process_pattern_scope_6: got unexpected plan from when clause 1"
            with engine.prove(rule.rule_base.root_name, 'knows_pattern_variable_scope', context,
                              ()) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "pattern_matching.post_process_pattern_scope_6: got unexpected plan from when clause 2"
                engine.get_ke('questions', 'pattern_scope').reset()
                with engine.prove(rule.rule_base.root_name, 'knows_how_patterns_match', context,
                                  ()) \
                  as gen_4:
                  for x_4 in gen_4:
                    assert x_4 is None, \
                      "pattern_matching.post_process_pattern_scope_6: got unexpected plan from when clause 4"
                    rule.rule_base.num_bc_rule_successes += 1
                    yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def knows_rest_variable(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(itertools.imap(lambda pat, arg:
                              pat.match_pattern(context, context,
                                                arg, arg_context),
                            patterns,
                            arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'rest_pattern_variable_syntax', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "pattern_matching.knows_rest_variable: got unexpected plan from when clause 1"
            with engine.prove(rule.rule_base.root_name, 'knows_rest_match', context,
                              ()) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "pattern_matching.knows_rest_variable: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def knows_rest_match(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(itertools.imap(lambda pat, arg:
                              pat.match_pattern(context, context,
                                                arg, arg_context),
                            patterns,
                            arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'rest_match', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "pattern_matching.knows_rest_match: got unexpected plan from when clause 1"
            with engine.prove(rule.rule_base.root_name, 'post_process_rest_match', context,
                              (rule.pattern(0),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "pattern_matching.knows_rest_match: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def post_process_rest_match_1(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(itertools.imap(lambda pat, arg:
                              pat.match_pattern(context, context,
                                                arg, arg_context),
                            patterns,
                            arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        engine.get_ke('questions', 'rest_match').reset()
        with engine.prove(rule.rule_base.root_name, 'knows_rest_match', context,
                          ()) \
          as gen_2:
          for x_2 in gen_2:
            assert x_2 is None, \
              "pattern_matching.post_process_rest_match_1: got unexpected plan from when clause 2"
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def post_process_rest_match_4_5(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(itertools.imap(lambda pat, arg:
                              pat.match_pattern(context, context,
                                                arg, arg_context),
                            patterns,
                            arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        if context.lookup_data('ans') in (4, 5):
          with engine.prove('special', 'claim_goal', context,
                            ()) \
            as gen_2:
            for x_2 in gen_2:
              assert x_2 is None, \
                "pattern_matching.post_process_rest_match_4_5: got unexpected plan from when clause 2"
              engine.get_ke('questions', 'rest_match').reset()
              with engine.prove(rule.rule_base.root_name, 'knows_rest_variable', context,
                                ()) \
                as gen_4:
                for x_4 in gen_4:
                  assert x_4 is None, \
                    "pattern_matching.post_process_rest_match_4_5: got unexpected plan from when clause 4"
                  rule.rule_base.num_bc_rule_successes += 1
                  yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def post_process_rest_match_correct(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(itertools.imap(lambda pat, arg:
                              pat.match_pattern(context, context,
                                                arg, arg_context),
                            patterns,
                            arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        if context.lookup_data('ans') in (2, 3):
          rule.rule_base.num_bc_rule_successes += 1
          yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def knows_tuple_patterns(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(itertools.imap(lambda pat, arg:
                              pat.match_pattern(context, context,
                                                arg, arg_context),
                            patterns,
                            arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'tuple_pattern_syntax', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "pattern_matching.knows_tuple_patterns: got unexpected plan from when clause 1"
            with engine.prove(rule.rule_base.root_name, 'knows_rest_variable', context,
                              ()) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "pattern_matching.knows_tuple_patterns: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def populate(engine):
  This_rule_base = engine.get_create('pattern_matching')
  
  bc_rule.bc_rule('knows_pattern_matching', This_rule_base, 'knows_pattern_matching',
                  knows_pattern_matching, None,
                  (),
                  (),
                  ())
  
  bc_rule.bc_rule('knows_pattern_matching_2', This_rule_base, 'knows_pattern_matching',
                  knows_pattern_matching_2, None,
                  (),
                  (),
                  ())
  
  bc_rule.bc_rule('knows_pat_master', This_rule_base, 'knows_pat_master',
                  knows_pat_master, None,
                  (),
                  (),
                  (pattern.pattern_literal(13),))
  
  bc_rule.bc_rule('learned_pattern_matching', This_rule_base, 'learned_pattern_matching',
                  learned_pattern_matching, None,
                  (),
                  (),
                  ())
  
  bc_rule.bc_rule('taught_pattern_matching_1_2_4_16', This_rule_base, 'taught_pattern_matching',
                  taught_pattern_matching_1_2_4_16, None,
                  (),
                  (),
                  (contexts.variable('ans'),))
  
  bc_rule.bc_rule('taught_pattern_matching_3_5_6_9_15', This_rule_base, 'taught_pattern_matching',
                  taught_pattern_matching_3_5_6_9_15, None,
                  (),
                  (),
                  (contexts.variable('ans'),))
  
  bc_rule.bc_rule('taught_pattern_matching_7_8_10', This_rule_base, 'taught_pattern_matching',
                  taught_pattern_matching_7_8_10, None,
                  (),
                  (),
                  (contexts.variable('ans'),))
  
  bc_rule.bc_rule('taught_pattern_matching_11_12', This_rule_base, 'taught_pattern_matching',
                  taught_pattern_matching_11_12, None,
                  (),
                  (),
                  (contexts.variable('ans'),))
  
  bc_rule.bc_rule('taught_pattern_matching_14', This_rule_base, 'taught_pattern_matching',
                  taught_pattern_matching_14, None,
                  (),
                  (),
                  (contexts.variable('ans'),))
  
  bc_rule.bc_rule('knows_pattern_variable_syntax', This_rule_base, 'knows_pattern_variable_syntax',
                  knows_pattern_variable_syntax, None,
                  (),
                  (),
                  (contexts.variable('ans'),))
  
  bc_rule.bc_rule('reset_if_wrong__right', This_rule_base, 'reset_if_wrong',
                  reset_if_wrong__right, None,
                  (contexts.anonymous('_'),
                   contexts.variable('right_ans'),
                   contexts.variable('right_ans'),),
                  (),
                  ())
  
  bc_rule.bc_rule('reset_if_wrong__wrong', This_rule_base, 'reset_if_wrong',
                  reset_if_wrong__wrong, None,
                  (contexts.variable('question'),
                   contexts.anonymous('_'),
                   contexts.anonymous('_'),),
                  (),
                  ())
  
  bc_rule.bc_rule('knows_patterns', This_rule_base, 'knows_patterns',
                  knows_patterns, None,
                  (),
                  (),
                  ())
  
  bc_rule.bc_rule('knows_literal_patterns', This_rule_base, 'knows_literal_patterns',
                  knows_literal_patterns, None,
                  (),
                  (),
                  (pattern.pattern_literal('pat_literal'),
                   pattern.pattern_literal(6),))
  
  bc_rule.bc_rule('ask_until_correct__ask', This_rule_base, 'ask_until_correct',
                  ask_until_correct__ask, None,
                  (contexts.variable('question'),
                   contexts.variable('right_ans'),),
                  (),
                  (contexts.variable('right_ans'),))
  
  bc_rule.bc_rule('ask_until_correct__try_again', This_rule_base, 'ask_until_correct',
                  ask_until_correct__try_again, None,
                  (contexts.variable('question'),
                   contexts.variable('right_ans'),),
                  (),
                  (contexts.variable('question'),
                   contexts.variable('right_ans'),))
  
  bc_rule.bc_rule('knows_pattern_variables', This_rule_base, 'knows_pattern_variables',
                  knows_pattern_variables, None,
                  (),
                  (),
                  ())
  
  bc_rule.bc_rule('knows_pattern_variable_scope', This_rule_base, 'knows_pattern_variable_scope',
                  knows_pattern_variable_scope, None,
                  (),
                  (),
                  (pattern.pattern_literal('multiple_matching'),
                   pattern.pattern_literal(4),
                   contexts.anonymous('_'),
                   pattern.pattern_literal('anonymous_matching'),
                   pattern.pattern_literal(3),))
  
  bc_rule.bc_rule('knows_how_patterns_match', This_rule_base, 'knows_how_patterns_match',
                  knows_how_patterns_match, None,
                  (),
                  (),
                  (contexts.variable('ans'),
                   pattern.pattern_literal('anonymous_matching'),
                   pattern.pattern_literal(3),))
  
  bc_rule.bc_rule('post_process_pattern_scope_1', This_rule_base, 'post_process_pattern_scope',
                  post_process_pattern_scope_1, None,
                  (pattern.pattern_literal(1),),
                  (),
                  ())
  
  bc_rule.bc_rule('post_process_pattern_scope_2', This_rule_base, 'post_process_pattern_scope',
                  post_process_pattern_scope_2, None,
                  (pattern.pattern_literal(2),),
                  (),
                  ())
  
  bc_rule.bc_rule('post_process_pattern_scope_3', This_rule_base, 'post_process_pattern_scope',
                  post_process_pattern_scope_3, None,
                  (pattern.pattern_literal(3),),
                  (),
                  ())
  
  bc_rule.bc_rule('post_process_pattern_scope_4', This_rule_base, 'post_process_pattern_scope',
                  post_process_pattern_scope_4, None,
                  (pattern.pattern_literal(4),),
                  (),
                  (contexts.anonymous('_'),))
  
  bc_rule.bc_rule('post_process_pattern_scope_5', This_rule_base, 'post_process_pattern_scope',
                  post_process_pattern_scope_5, None,
                  (pattern.pattern_literal(5),),
                  (),
                  (contexts.anonymous('_'),))
  
  bc_rule.bc_rule('post_process_pattern_scope_6', This_rule_base, 'post_process_pattern_scope',
                  post_process_pattern_scope_6, None,
                  (pattern.pattern_literal(6),),
                  (),
                  ())
  
  bc_rule.bc_rule('knows_rest_variable', This_rule_base, 'knows_rest_variable',
                  knows_rest_variable, None,
                  (),
                  (),
                  (contexts.anonymous('_'),))
  
  bc_rule.bc_rule('knows_rest_match', This_rule_base, 'knows_rest_match',
                  knows_rest_match, None,
                  (),
                  (),
                  (contexts.variable('ans'),))
  
  bc_rule.bc_rule('post_process_rest_match_1', This_rule_base, 'post_process_rest_match',
                  post_process_rest_match_1, None,
                  (pattern.pattern_literal(1),),
                  (),
                  ())
  
  bc_rule.bc_rule('post_process_rest_match_4_5', This_rule_base, 'post_process_rest_match',
                  post_process_rest_match_4_5, None,
                  (contexts.variable('ans'),),
                  (),
                  ())
  
  bc_rule.bc_rule('post_process_rest_match_correct', This_rule_base, 'post_process_rest_match',
                  post_process_rest_match_correct, None,
                  (contexts.variable('ans'),),
                  (),
                  ())
  
  bc_rule.bc_rule('knows_tuple_patterns', This_rule_base, 'knows_tuple_patterns',
                  knows_tuple_patterns, None,
                  (),
                  (),
                  (contexts.anonymous('_'),))


Krb_filename = '../pattern_matching.krb'
Krb_lineno_map = (
    ((16, 20), (41, 41)),
    ((22, 22), (43, 43)),
    ((23, 28), (44, 44)),
    ((41, 45), (47, 47)),
    ((47, 52), (49, 49)),
    ((65, 69), (52, 52)),
    ((71, 76), (54, 54)),
    ((89, 93), (57, 57)),
    ((95, 100), (59, 59)),
    ((101, 106), (60, 60)),
    ((119, 123), (63, 63)),
    ((125, 130), (65, 65)),
    ((131, 131), (66, 66)),
    ((132, 137), (67, 67)),
    ((138, 143), (68, 68)),
    ((144, 149), (69, 69)),
    ((150, 155), (70, 70)),
    ((168, 172), (73, 73)),
    ((174, 179), (75, 75)),
    ((180, 180), (76, 76)),
    ((181, 186), (77, 77)),
    ((199, 203), (80, 80)),
    ((205, 210), (82, 82)),
    ((211, 211), (83, 83)),
    ((212, 217), (84, 84)),
    ((230, 234), (87, 87)),
    ((236, 241), (89, 89)),
    ((242, 242), (90, 90)),
    ((243, 248), (91, 91)),
    ((261, 265), (94, 94)),
    ((267, 272), (96, 96)),
    ((273, 273), (97, 97)),
    ((274, 279), (98, 98)),
    ((280, 285), (99, 99)),
    ((298, 302), (102, 102)),
    ((304, 309), (104, 104)),
    ((322, 326), (108, 108)),
    ((328, 333), (110, 110)),
    ((346, 350), (113, 113)),
    ((352, 352), (115, 115)),
    ((365, 369), (118, 118)),
    ((371, 376), (120, 120)),
    ((377, 382), (121, 121)),
    ((383, 388), (122, 122)),
    ((401, 405), (125, 125)),
    ((407, 413), (127, 127)),
    ((426, 430), (130, 130)),
    ((432, 437), (132, 132)),
    ((438, 443), (133, 133)),
    ((456, 460), (136, 136)),
    ((462, 462), (138, 138)),
    ((463, 463), (139, 139)),
    ((464, 470), (140, 140)),
    ((483, 487), (143, 143)),
    ((489, 494), (145, 145)),
    ((495, 500), (146, 146)),
    ((513, 517), (149, 149)),
    ((519, 525), (151, 151)),
    ((526, 531), (152, 152)),
    ((532, 538), (153, 153)),
    ((551, 555), (156, 156)),
    ((557, 562), (158, 158)),
    ((563, 568), (159, 159)),
    ((569, 575), (160, 160)),
    ((588, 592), (163, 163)),
    ((594, 599), (165, 165)),
    ((600, 605), (166, 166)),
    ((606, 606), (167, 167)),
    ((607, 612), (168, 168)),
    ((625, 629), (171, 171)),
    ((631, 636), (173, 173)),
    ((637, 637), (174, 174)),
    ((638, 643), (175, 175)),
    ((656, 660), (178, 178)),
    ((674, 678), (181, 181)),
    ((680, 685), (183, 183)),
    ((686, 691), (184, 184)),
    ((692, 692), (185, 185)),
    ((693, 698), (186, 186)),
    ((711, 715), (189, 189)),
    ((717, 722), (191, 191)),
    ((723, 723), (192, 192)),
    ((724, 729), (193, 193)),
    ((742, 746), (196, 196)),
    ((748, 753), (198, 198)),
    ((754, 759), (199, 199)),
    ((760, 760), (200, 200)),
    ((761, 766), (201, 201)),
    ((779, 783), (204, 204)),
    ((785, 790), (206, 206)),
    ((791, 796), (207, 207)),
    ((809, 813), (210, 210)),
    ((815, 820), (212, 212)),
    ((821, 826), (213, 213)),
    ((839, 843), (216, 216)),
    ((845, 845), (218, 218)),
    ((846, 851), (219, 219)),
    ((864, 868), (222, 222)),
    ((870, 870), (224, 224)),
    ((871, 876), (225, 225)),
    ((877, 877), (226, 226)),
    ((878, 883), (227, 227)),
    ((896, 900), (230, 230)),
    ((902, 902), (232, 232)),
    ((915, 919), (235, 235)),
    ((921, 926), (237, 237)),
    ((927, 932), (238, 238)),
)
