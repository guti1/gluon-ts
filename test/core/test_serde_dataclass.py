# Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License").
# You may not use this file except in compliance with the License.
# A copy of the License is located at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# or in the "license" file accompanying this file. This file is distributed
# on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either
# express or implied. See the License for the specific language governing
# permissions and limitations under the License.

from typing import List

from gluonts.core import serde


@serde.dataclass
class Estimator:
    prediction_length: int
    context_length: int = serde.OrElse(
        lambda prediction_length: prediction_length * 2
    )

    use_feat_static_cat: bool = True
    cardinality: List[int] = serde.EVENTUAL

    def __eventually__(self, cardinality):
        if not self.use_feat_static_cat:
            cardinality.set([1])
        else:
            cardinality.set_default([1])


def test_dataclass():
    est = Estimator(prediction_length=7)

    assert est.prediction_length == 7
    assert est.context_length == 14
    assert est.cardinality == [1]
