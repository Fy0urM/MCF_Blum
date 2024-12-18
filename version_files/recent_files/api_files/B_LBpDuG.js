import {
  d as A,
  u as U,
  F as m,
  P as h,
  d2 as _,
  S as k,
  a8 as b,
  a as r,
  c as o,
  b as p,
  t as y,
  e as a,
  w as E,
  g as d,
  n as P,
  d3 as C,
  j as N
} from "./BZXAykfw.js";
const S = {
    class: "circle"
  },
  x = {
    class: "letters"
  },
  B = ["src"],
  D = {
    key: 0,
    src: C,
    alt: "Pokras smile",
    class: "pokras-smile"
  },
  F = A({
    __name: "AvatarPlain",
    props: {
      overrideAvatarUrl: {
        type: String,
        default: void 0
      },
      small: {
        type: Boolean,
        default: !1
      }
    },
    emits: ["onImageError"],
    setup(n) {
      const i = n,
        u = U().internal.isPokrasTheme,
        v = m(() => {
          var t, c;
          const e = h().$webApp.dataUnsafe.user,
            s = "X";
          if (e) {
            const f = e.last_name && ((t = _(e.last_name)) == null ? void 0 : t.toUpperCase()),
              g = (c = _(e.first_name)) == null ? void 0 : c.toUpperCase();
            return [f, g].join("") || s
          }
          return s
        }),
        l = m(() => {
          var s;
          if (i.overrideAvatarUrl) return i.overrideAvatarUrl;
          const e = (s = k().getters.getUser.value) == null ? void 0 : s.avatarUrl;
          if (e) return e
        });
      return (e, s) => {
        const t = b("img-loader");
        return r(), o("div", {
          class: P(["account-avatar-plain", {
            "is-small": n.small
          }])
        }, [p("div", S, [p("span", x, y(a(v)), 1), a(l) ? E((r(), o("img", {
          key: 0,
          src: a(l),
          alt: "Avatar",
          class: "img"
        }, null, 8, B)), [
          [t, {
            onError: () => e.$emit("onImageError")
          }]
        ]) : d("", !0)]), a(u) ? (r(), o("img", D)) : d("", !0)], 2)
      }
    }
  }),
  w = N(F, [
    ["__scopeId", "data-v-9b4fb5cf"]
  ]);
export {
  w as _
};