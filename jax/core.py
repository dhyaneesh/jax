# Copyright 2022 The JAX Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Note: import <name> as <name> is required for names to be exported.
# See PEP 484 & https://github.com/jax-ml/jax/issues/7570

from jax._src.core import (
  AbstractToken as AbstractToken,
  AbstractValue as AbstractValue,
  Atom as Atom,
  CallPrimitive as CallPrimitive,
  DebugInfo as DebugInfo,
  DShapedArray as DShapedArray,
  DropVar as DropVar,
  Effect as Effect,
  Effects as Effects,
  get_opaque_trace_state as get_opaque_trace_state,
  InconclusiveDimensionOperation as InconclusiveDimensionOperation,
  JaxprPpContext as JaxprPpContext,
  JaxprPpSettings as JaxprPpSettings,
  JaxprTypeError as JaxprTypeError,
  nonempty_axis_env as nonempty_axis_env_DO_NOT_USE,  # noqa: F401
  OutputType as OutputType,
  ParamDict as ParamDict,
  ShapedArray as ShapedArray,
  Trace as Trace,
  Tracer as Tracer,
  unsafe_am_i_under_a_jit as unsafe_am_i_under_a_jit_DO_NOT_USE,  # noqa: F401
  unsafe_am_i_under_a_vmap as unsafe_am_i_under_a_vmap_DO_NOT_USE,  # noqa: F401
  unsafe_get_axis_names as unsafe_get_axis_names_DO_NOT_USE,  # noqa: F401
  UnshapedArray as UnshapedArray,
  Value as Value,
  abstract_token as abstract_token,
  aval_mapping_handlers as aval_mapping_handlers,
  call as call,
  call_impl as call_impl,
  check_jaxpr as check_jaxpr,
  concrete_or_error as concrete_or_error,
  concretization_function_error as concretization_function_error,
  custom_typechecks as custom_typechecks,
  ensure_compile_time_eval as ensure_compile_time_eval,
  eval_context as eval_context,
  eval_jaxpr as eval_jaxpr,
  find_top_trace as find_top_trace,
  gensym as gensym,
  get_aval as get_aval,
  is_concrete as is_concrete,
  is_constant_dim as is_constant_dim,
  is_constant_shape as is_constant_shape,
  jaxprs_in_params as jaxprs_in_params,
  literalable_types as literalable_types,
  mapped_aval as mapped_aval,
  max_dim as max_dim,
  min_dim as min_dim,
  new_jaxpr_eqn as new_jaxpr_eqn,
  no_axis_name as no_axis_name,
  no_effects as no_effects,
  primal_dtype_to_tangent_dtype as primal_dtype_to_tangent_dtype,
  pytype_aval_mappings as pytype_aval_mappings,
  set_current_trace as set_current_trace,
  subjaxprs as subjaxprs,
  take_current_trace as take_current_trace,
  trace_ctx as trace_ctx,
  TraceTag as TraceTag,
  traverse_jaxpr_params as traverse_jaxpr_params,
  unmapped_aval as unmapped_aval,
  valid_jaxtype as valid_jaxtype,
)


from jax._src import core as _src_core
_deprecations = {
    # Added 2024-12-16
    "ClosedJaxpr": ("jax.core.ClosedJaxpr is deprecated. Use jax.extend.core.ClosedJaxpr instead, "
                    "and see https://jax.readthedocs.io/en/latest/jax.extend.html for details.",
                    _src_core.ClosedJaxpr),
    "Jaxpr": ("jax.core.Jaxpr is deprecated. Use jax.extend.core.Jaxpr instead, "
              "and see https://jax.readthedocs.io/en/latest/jax.extend.html for details.",
              _src_core.Jaxpr),
    "JaxprEqn": ("jax.core.JaxprEqn is deprecated. Use jax.extend.core.JaxprEqn instead, "
                 "and see https://jax.readthedocs.io/en/latest/jax.extend.html for details.",
                 _src_core.JaxprEqn),
    "Literal": ("jax.core.Literal is deprecated. Use jax.extend.core.Literal instead, "
                "and see https://jax.readthedocs.io/en/latest/jax.extend.html for details.",
                _src_core.Literal),
    "Primitive": ("jax.core.Primitive is deprecated. Use jax.extend.core.Primitive instead, "
                  "and see https://jax.readthedocs.io/en/latest/jax.extend.html for details.",
                  _src_core.Primitive),
    "Token": ("jax.core.Token is deprecated. Use jax.extend.core.Token instead, "
              "and see https://jax.readthedocs.io/en/latest/jax.extend.html for details.",
              _src_core.Token),
    "Var": ("jax.core.Var is deprecated. Use jax.extend.core.Var instead, "
            "and see https://jax.readthedocs.io/en/latest/jax.extend.html for details.",
            _src_core.Var),
    # Added 2024-12-11
    "axis_frame": ("jax.core.axis_frame is deprecated.", _src_core.axis_frame),
    "AxisName": ("jax.core.AxisName is deprecated.", _src_core.AxisName),
    "AxisSize": ("jax.core.AxisSize is deprecated.", _src_core.AxisSize),
    "ConcretizationTypeError": ("jax.core.ConcretizationTypeError is deprecated; "
                                "use jax.errors.ConcretizationTypeError.",
                                _src_core.ConcretizationTypeError),
    "EvalTrace": ("jax.core.EvalTrace is deprecated.", _src_core.EvalTrace),
    "InDBIdx": ("jax.core.InDBIdx is deprecated.", _src_core.InDBIdx),
    "InputType": ("jax.core.InputType is deprecated.", _src_core.InputType),
    "MapPrimitive": ("jax.core.MapPrimitive is deprecated.", _src_core.MapPrimitive),
    "OpaqueTraceState": ("jax.core.OpaqueTraceState is deprecated.", _src_core.OpaqueTraceState),
    "OutDBIdx": ("jax.core.OutDBIdx is deprecated.", _src_core.OutDBIdx),
    "TRACER_LEAK_DEBUGGER_WARNING": ("jax.core.TRACER_LEAK_DEBUGGER_WARNING is deprecated.",
                                     _src_core.TRACER_LEAK_DEBUGGER_WARNING),
    "call_p": ("jax.core.call_p is deprecated. Use jax.extend.core.primitives.call_p",
               _src_core.call_p),
    "closed_call_p": ("jax.core.closed_call_p is deprecated. Use jax.extend.core.primitives.closed_call_p",
                      _src_core.closed_call_p),
    "concrete_aval": ("jax.core.concrete_aval is deprecated.", _src_core.abstractify),
    "dedup_referents": ("jax.core.dedup_referents is deprecated.", _src_core.dedup_referents),
    "escaped_tracer_error": ("jax.core.escaped_tracer_error is deprecated.",
                             _src_core.escaped_tracer_error),
    "extend_axis_env_nd": ("jax.core.extend_axis_env_nd is deprecated.",
                           _src_core.extend_axis_env_nd),
    "get_type": ("jax.core.get_type is deprecated.", _src_core.get_aval),
    "get_referent": ("jax.core.get_referent is deprecated.", _src_core.get_referent),
    "join_effects": ("jax.core.join_effects is deprecated.", _src_core.join_effects),
    "leaked_tracer_error": ("jax.core.leaked_tracer_error is deprecated.",
                            _src_core.leaked_tracer_error),
    "maybe_find_leaked_tracers": ("jax.core.maybe_find_leaked_tracers is deprecated.",
                                  _src_core.maybe_find_leaked_tracers),
    "raise_to_shaped_mappings": ("jax.core.raise_to_shaped_mappings is deprecated."
                                 " It is unused as of jax v0.4.36.",
                                 _src_core.raise_to_shaped_mappings),
    "reset_trace_state": ("jax.core.reset_trace_state is deprecated.",
                          _src_core.reset_trace_state),
    "str_eqn_compact": ("jax.core.str_eqn_compact is deprecated.", _src_core.str_eqn_compact),
    "substitute_vars_in_output_ty": ("jax.core.substitute_vars_in_output_ty is deprecated.",
                                     _src_core.substitute_vars_in_output_ty),
    "trace_state_clean": ("jax.core.trace_state_clean is deprecated.",
                          _src_core.trace_state_clean),
    "typecheck": ("jax.core.typecheck is deprecated.", _src_core.typecheck),
    "typecompat": ("jax.core.typecompat is deprecated.", _src_core.typecompat),
    "typematch": ("jax.core.typematch is deprecated.", _src_core.typematch),
    "used_axis_names_jaxpr": ("jax.core.used_axis_names_jaxpr is deprecated.",
                              _src_core.used_axis_names_jaxpr),
    # Added 2024-12-10
    "full_lower": ("jax.core.full_lower is deprecated. It is a no-op as of JAX v0.4.36.",
                   _src_core.full_lower),
    "jaxpr_as_fun": ("jax.core.jaxpr_as_fun is deprecated. Use jax.extend.core.jaxpr_as_fun instead, "
                     "and see https://jax.readthedocs.io/en/latest/jax.extend.html for details.",
                     _src_core.jaxpr_as_fun),
    "lattice_join": ("jax.core.lattice_join is deprecated. It is a no-op as of JAX v0.4.36.",
                     _src_core.lattice_join),
    "raise_to_shaped": ("jax.core.raise_to_shaped is deprecated. It is a no-op as of JAX v0.4.36.",
                        _src_core.raise_to_shaped),
}

import typing
if typing.TYPE_CHECKING:
  AxisName = _src_core.AxisName
  AxisSize = _src_core.AxisSize
  ClosedJaxpr = _src_core.ClosedJaxpr
  ConcretizationTypeError = _src_core.ConcretizationTypeError
  EvalTrace = _src_core.EvalTrace
  InDBIdx = _src_core.InDBIdx
  InputType = _src_core.InputType
  Jaxpr = _src_core.Jaxpr
  JaxprEqn = _src_core.JaxprEqn
  Literal = _src_core.Literal
  MapPrimitive = _src_core.MapPrimitive
  OpaqueTraceState = _src_core.OpaqueTraceState
  OutDBIdx = _src_core.OutDBIdx
  Primitive = _src_core.Primitive
  Token = _src_core.Token
  TRACER_LEAK_DEBUGGER_WARNING = _src_core.TRACER_LEAK_DEBUGGER_WARNING
  Var = _src_core.Var
  axis_frame = _src_core.axis_frame
  call_p = _src_core.call_p
  closed_call_p = _src_core.closed_call_p
  concrete_aval = _src_core.abstractify
  dedup_referents = _src_core.dedup_referents
  escaped_tracer_error = _src_core.escaped_tracer_error
  extend_axis_env_nd = _src_core.extend_axis_env_nd
  full_lower = _src_core.full_lower
  get_type = _src_core.get_aval
  get_referent = _src_core.get_referent
  jaxpr_as_fun = _src_core.jaxpr_as_fun
  join_effects = _src_core.join_effects
  lattice_join = _src_core.lattice_join
  leaked_tracer_error = _src_core.leaked_tracer_error
  maybe_find_leaked_tracers = _src_core.maybe_find_leaked_tracers
  raise_to_shaped = _src_core.raise_to_shaped
  raise_to_shaped_mappings = _src_core.raise_to_shaped_mappings
  reset_trace_state = _src_core.reset_trace_state
  str_eqn_compact = _src_core.str_eqn_compact
  substitute_vars_in_output_ty = _src_core.substitute_vars_in_output_ty
  trace_state_clean = _src_core.trace_state_clean
  typecheck = _src_core.typecheck
  typecompat = _src_core.typecompat
  typematch = _src_core.typematch
  used_axis_names_jaxpr = _src_core.used_axis_names_jaxpr
else:
  from jax._src.deprecations import deprecation_getattr as _deprecation_getattr
  __getattr__ = _deprecation_getattr(__name__, _deprecations)
  del _deprecation_getattr
del typing
del _src_core
