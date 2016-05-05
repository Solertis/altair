# This file auto-generated by altair.schema.parser.write_files().
# do not modify directly.

import traitlets as T
from ..baseobject import BaseObject
from .facetscaleconfig import FacetScaleConfig
from .cellconfig import CellConfig
from .facetgridconfig import FacetGridConfig
from .axisconfig import AxisConfig


class FacetConfig(BaseObject):
    scale = T.Instance(FacetScaleConfig, default_value=None, allow_none=True)
    cell = T.Instance(CellConfig, default_value=None, allow_none=True)
    grid = T.Instance(FacetGridConfig, default_value=None, allow_none=True)
    axis = T.Instance(AxisConfig, default_value=None, allow_none=True)
